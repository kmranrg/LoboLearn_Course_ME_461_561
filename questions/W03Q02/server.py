import random

def generate(data):
    seed = data.get("variant_seed", 42)  
    rng = random.Random(seed)

    function_names = ["ReLU", "Sigmoid", "Tanh", "Linear"]
    function_formulas = {
        "ReLU": r"\[ f(x) = \max(0, x) \]",
        "Sigmoid": r"\[ f(x) = \frac{1}{1 + e^{-x}} \]",
        "Tanh": r"\[ f(x) = \tanh(x) \]",
        "Linear": r"\[ f(x) = x \]"
    }

    index = seed % len(function_names)
    correct_name = function_names[index]
    correct_formula = function_formulas[correct_name]

    distractors = [name for name in function_names if name != correct_name]
    wrong_choices = rng.sample(distractors, 2)

    # Combine and shuffle choices
    choices = [{"text": correct_name, "correct": True}] + \
              [{"text": d, "correct": False} for d in wrong_choices]
    rng.shuffle(choices)

    # Send to frontend
    data["params"]["formula"] = correct_formula
    data["params"]["choices"] = choices

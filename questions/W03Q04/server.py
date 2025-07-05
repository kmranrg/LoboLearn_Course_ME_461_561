import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 2025))

    correct = "They introduce non-linearity between layers, allowing the network to model complex patterns."

    distractors = [
        "They normalize the outputs of each layer to stay between 0 and 1.",
        "They reduce the number of parameters by filtering weights.",
        "They allow gradients to flow without any transformation during backpropagation."
    ]

    choices = [{"text": correct, "correct": True}] + \
              [{"text": d, "correct": False} for d in rng.sample(distractors, 2)]
    rng.shuffle(choices)

    data["params"]["choices"] = choices

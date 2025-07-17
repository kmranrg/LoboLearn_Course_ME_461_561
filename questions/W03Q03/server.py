import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 1001))

    correct = "The use of non-linear activation functions applied to the weighted sum."

    distractors = [
        "The use of gradient descent instead of closed-form solutions.",
        "The presence of a bias term in the model.",
        "The ability to process categorical features directly."
    ]

    selected = [{"text": correct, "correct": True}] + \
               [{"text": d, "correct": False} for d in rng.sample(distractors, 2)]

    rng.shuffle(selected)
    data["params"]["choices"] = selected

import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 2026))

    correct = "A decision boundary that separates the two classes with a linear function."

    distractors = [
        "The exact probability that a sample belongs to each class.",
        "The number of neurons required in the hidden layer.",
        "The best activation function to use in a deep network."
    ]

    choices = [{"text": correct, "correct": True}] + \
              [{"text": d, "correct": False} for d in rng.sample(distractors, 2)]
    rng.shuffle(choices)

    data["params"]["choices"] = choices

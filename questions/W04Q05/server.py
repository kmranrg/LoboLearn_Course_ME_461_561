import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 2027))

    correct = "A linear decision boundary and the probability that an input belongs to a particular class."

    distractors = [
        "An exact boundary that perfectly separates all data points.",
        "The number of clusters in the input data.",
        "The number of hidden layers needed in a neural network."
    ]

    choices = [{"text": correct, "correct": True}] + \
              [{"text": d, "correct": False} for d in rng.sample(distractors, 2)]
    rng.shuffle(choices)

    data["params"]["choices"] = choices

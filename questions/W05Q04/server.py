import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 5201))

    correct = (
        "It lets the SVM compute inner products in a higher-dimensional feature space "
        "without ever computing the coordinates of that space explicitly."
    )

    distractors = [
        "It randomly projects the data into many subspaces and averages the results.",
        "It forces all support vectors to have the same norm for numerical stability.",
        "It guarantees zero training error by adding one feature per training sample."
    ]

    # pick two random distractors
    selected = rng.sample(distractors, 2)

    choices = (
        [{"text": correct, "correct": True}] +
        [{"text": d, "correct": False} for d in selected]
    )
    rng.shuffle(choices)

    data["params"]["choices"] = choices

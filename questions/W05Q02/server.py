import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 5301))

    correct = (
        "Maximizing the margin makes the classifier more robust, "
        "because even small perturbations of the data are less likely to change the decision."
    )

    distractors = [
        "It reduces the number of support vectors needed for prediction to zero.",
        "It guarantees that every point is classified with 100 % confidence.",
        "It minimizes the sum of squared distances between all data points and the hyperplane."
    ]

    # pick two random distractors
    chosen_distractors = rng.sample(distractors, 2)

    choices = (
        [{"text": correct, "correct": True}] +
        [{"text": d, "correct": False} for d in chosen_distractors]
    )
    rng.shuffle(choices)

    data["params"]["choices"] = choices

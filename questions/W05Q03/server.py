import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 5310))

    correct = "Only the support vectors (the points that lie on the margin)."

    distractors = [
        "All points from both classes equally.",
        "Only the points closest to the class centroids.",
        "Randomly selected points to reduce computation."
    ]

    choices = [{"text": correct, "correct": True}] + \
              [{"text": d, "correct": False} for d in rng.sample(distractors, 2)]
    rng.shuffle(choices)

    data["params"]["choices"] = choices

import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 6123))

    # Correct statement (weaker covariance is in Plot B, right-hand cloud)
    correct = (
        "Plot&nbsp;B shows a much weaker linear correlation between "
        "$Y_1$ and $Y_2$ than Plot&nbsp;A."
    )

    # ≥5 distractors – now 7 distinct wrong statements
    distractors = [
        "Plot&nbsp;B has a stronger positive covariance than Plot&nbsp;A.",
        "Plot&nbsp;B exhibits a clear negative (downward) correlation.",
        "Plot&nbsp;B has a larger variance along the $Y_1=Y_2$ direction than Plot&nbsp;A.",
        "Plot&nbsp;B’s samples are more tightly clustered because its covariance matrix is zero.",
        "Plot&nbsp;B displays perfect independence (zero covariance) just like Plot&nbsp;A.",
        "Plot&nbsp;B’s scatter is elongated more than Plot&nbsp;A, indicating higher covariance.",
        "Plot&nbsp;B forms an L-shaped pattern, so its covariance cannot be compared."
    ]

    # Build answer list: correct + 2 random distractors
    choices = ([{"text": correct, "correct": True}] +
               [{"text": d, "correct": False} for d in rng.sample(distractors, 2)])
    rng.shuffle(choices)

    data["params"]["choices"] = choices

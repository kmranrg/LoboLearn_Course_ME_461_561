import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 6301))

    # Correct statement
    correct = "Plot (A) shows the negative covariance."

    # ≥ 5 distractor statements
    distractors = [
        "Plot (B) shows the negative covariance.",
        "Both plots have zero covariance between the variables.",
        "Neither plot has any linear relationship between the variables.",
        "Plot (A) actually has a stronger positive covariance than Plot (B).",
        "Plot (A) and Plot (B) display identical covariance magnitudes.",
        "The covariance of both plots is undefined because of the sample size."
    ]

    # Build answer list: correct + 2 random distractors
    choices = [{"text": correct, "correct": True}] + \
              [{"text": d, "correct": False} for d in rng.sample(distractors, 2)]
    rng.shuffle(choices)

    data["params"]["choices"] = choices

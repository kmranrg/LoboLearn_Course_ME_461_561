import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 6201))

    # Correct answer – stronger covariance is in Plot A.
    correct = "Plot (A) shows the stronger covariance between returns."

    # 7 distinct distractors ( ≥5 as requested )
    distractors = [
        "Plot (B) shows the stronger covariance between returns.",
        "Both plots have identical covariance.",
        "Neither plot exhibits any linear relationship.",
        "Plot (A) actually depicts zero covariance.",
        "Plot (B) shows negative covariance, which is stronger in magnitude.",
        "Covariance cannot be compared here because the axes are different scales.",
        "The strength of covariance is impossible to judge without regression lines."
    ]

    # Pick any 2 distractors for this variant
    selected = rng.sample(distractors, 2)

    # Assemble choice list
    choices = [{"text": correct, "correct": True}] + \
              [{"text": d, "correct": False} for d in selected]
    rng.shuffle(choices)

    data["params"]["choices"] = choices

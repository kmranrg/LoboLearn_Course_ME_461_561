import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 6501))

    # Correct answer — Plot B (right) has the positive covariance
    correct = "Plot&nbsp;B shows the positive covariance between \(Y_1\) and \(Y_2\)."

    # ≥ 5 distractors
    distractors = [
        "Plot&nbsp;A shows the positive covariance between \(Y_1\) and \(Y_2\).",
        "Both plots display zero covariance.",
        "Plot&nbsp;B actually has a strong <em>negative</em> covariance.",
        "Neither plot has any discernible linear pattern.",
        "Plot&nbsp;B’s variables are independent, so its covariance is exactly zero.",
        "Plot&nbsp;B has higher variance but the same covariance sign as Plot&nbsp;A.",
        "Covariance cannot be determined because the axes are on different scales."
    ]

    # random two wrong statements each variant
    selected = rng.sample(distractors, 2)

    choices = (
        [{"text": correct, "correct": True}] +
        [{"text": d, "correct": False} for d in selected]
    )
    rng.shuffle(choices)

    data["params"]["choices"] = choices

import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 7201))

    # single correct statement
    correct = (
        "The kernel encodes how strongly any two inputs are expected to co-vary; "
        "it defines the covariance between function values so the GP can "
        "interpolate smoothly between observations."
    )

    # pool of ≥ 5 plausible but wrong statements
    distractors = [
        "The kernel sets the global mean of the GP prior.",
        "The kernel determines the numerical method used to invert the covariance matrix.",
        "The kernel fixes the observation noise level \(\\sigma_n^2\\).",
        "The kernel specifies the dimension of the input space.",
        "The kernel forces all training residuals to be exactly zero.",
        "The kernel merely scales the training targets into the range [0,1]."
    ]

    # choose 2 wrong statements each variant
    chosen = rng.sample(distractors, 2)

    # assemble & shuffle
    choices = (
        [{"text": correct, "correct": True}] +
        [{"text": d, "correct": False} for d in chosen]
    )
    rng.shuffle(choices)
    data["params"]["choices"] = choices

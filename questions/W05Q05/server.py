import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 5401))

    correct = (
        "The kernel must generate a symmetric and positive-semidefinite "
        "Gram matrix for any finite set of input points (Mercer condition)."
    )

    distractors = [
        "It must output values strictly between 0 and 1 for all input pairs.",
        "It must be differentiable with respect to both inputs everywhere.",
        "It must map inputs to an infinite-dimensional space."
    ]

    # choose two distractors at random
    chosen = rng.sample(distractors, 2)

    data["params"]["choices"] = (
        [{"text": correct, "correct": True}] +
        [{"text": d, "correct": False} for d in chosen]
    )
    random.shuffle(data["params"]["choices"])

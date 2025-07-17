import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 7302))

    # One correct explanation of gamma
    correct = (
        "It geometrically down‑weights rewards that occur further in the future, "
        "trading off immediacy versus long‑term gain and ensuring the infinite "
        "sum converges."
    )

    # ≥ 5 plausible but wrong statements
    distractors = [
        "It rescales the reward so that all returns lie strictly between –1 and 1.",
        "It guarantees the agent will eventually take every possible action.",
        "It acts as a learning‑rate parameter for the value‑function update rule.",
        "It forces the environment’s dynamics to become deterministic.",
        "It removes any influence of the immediate reward so the agent focuses only on long‑term outcomes.",
        "It normalises rewards so that their variance is always exactly one."
    ]

    # Choose two distinct wrong statements for this variant
    chosen = rng.sample(distractors, 2)

    # Assemble choices and shuffle order
    choices = (
        [{"text": correct, "correct": True}] +
        [{"text": d, "correct": False} for d in chosen]
    )
    rng.shuffle(choices)

    data["params"]["choices"] = choices

import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 7301))

    # Correct statement about the RL objective
    correct = (
        "Learn a policy that maximises the <em>expected</em> cumulative "
        "discounted reward (return) over time."
    )

    # Pool of ≥ 5 plausible‑but‑wrong statements
    distractors = [
        "Select the single action that yields the largest immediate reward "
        "and repeat it forever.",
        "Minimise the variance of the reward signal, regardless of its sign.",
        "Learn a value function so that the return is exactly zero at every step.",
        "Maximise the time spent exploring without considering rewards.",
        "Keep the agent’s policy fixed and instead modify the environment to "
        "increase observed rewards.",
        "Guarantee that every state is visited equally often, even if it "
        "reduces cumulative reward."
    ]

    # Pick two random distractors for this variant
    chosen = rng.sample(distractors, 2)

    # Assemble and shuffle
    choices = (
        [{"text": correct, "correct": True}] +
        [{"text": d, "correct": False} for d in chosen]
    )
    rng.shuffle(choices)

    data["params"]["choices"] = choices

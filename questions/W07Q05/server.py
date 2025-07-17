import random


def generate(data):
    """Create answer options about the role of EPSILON."""
    rng = random.Random(data.get("variant_seed", 7401))

    correct = (
        "It sets the probability of choosing the greedy (best‑known) "
        "action—about 90% exploit and 10% explore in this script."
    )

    distractors_pool = [
        "It is the learning‑rate multiplier used when updating Q‑values.",
        "It scales the discount factor γ on future rewards.",
        "It limits how far the agent can move to the right in one episode.",
        "It controls how quickly the episode time steps are printed "
        "(<code>FRESH_TIME</code> is the one that does).",
        "It forces the agent to alternate strictly between left and right moves."
    ]

    # pick three random incorrect statements each variant
    distractors = rng.sample(distractors_pool, 3)

    choices = ([{"text": correct, "correct": True}] +
               [{"text": d, "correct": False} for d in distractors])
    rng.shuffle(choices)

    data["params"]["choices"] = choices

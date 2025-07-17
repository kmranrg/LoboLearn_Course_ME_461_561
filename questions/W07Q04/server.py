import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 7301))

    # One correct relational fact
    correct = (
        "For every state&nbsp;\\(s\\), "
        "the state‑value function equals the "
        "policy‑weighted action values:&nbsp;"
        "$V_{\\pi}(s)=\\sum_{a\\in\\mathcal{A}} \\pi(a\\mid s)\\,q_{\\pi}(s,a).$"
    )

    # Plausible but incorrect statements
    distractor_pool = [
        "The action‑value function is always the maximum of the state values "
        "over all actions.",
        "The state‑value function ignores future rewards, "
        "whereas the action‑value function includes them.",
        "At an optimal policy, $V_{\\pi}(s)$ and $q_{\\pi}(s,a)$ "
        "are identical for every action $a$.",
        "$q_{\\pi}(s,a)$ is defined only for deterministic policies, "
        "whereas $V_{\\pi}(s)$ allows stochastic policies.",
        "The two functions are unrelated; "
        "they are computed from disjoint sets of trajectories.",
    ]

    # Randomly pick three distractors each variant
    distractors = rng.sample(distractor_pool, 3)

    # Build shuffled choice list
    choices = [{"text": correct, "correct": True}] + \
              [{"text": d, "correct": False} for d in distractors]
    rng.shuffle(choices)

    data["params"]["choices"] = choices

import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 7201))

    # Canonical 5‑tuple parts
    canonical = [
        ("The state set \\(\\mathcal{S}\\).", True),
        ("The action set \\(\\mathcal{A}\\).", True),
        ("The transition function \\(T(s'\\mid s,a)\\).", True),
        ("The reward function \\(r(s,a)\\).", True),
        ("The discount factor \\(\\gamma\\).", True),
    ]

    # Plausible but *not* part of the formal tuple
    distractor_pool = [
        "A policy \\(\\pi(a\\mid s)\\).",
        "The state–value function \\(V^{\\pi}(s)\\).",
        "The action–value function \\(Q^{\\pi}(s,a)\\).",
        "A replay buffer of past transitions.",
        "An exploration rate \\(\\varepsilon\\).",
        "A terminal cost function.",
    ]

    # Choose one real component as the correct answer
    correct_text, _ = rng.choice(canonical)
    correct_entry = {"text": correct_text, "correct": True}

    # Pick three unique distractors each time
    distractors = rng.sample(distractor_pool, 3)
    distractor_entries = [{"text": d, "correct": False} for d in distractors]

    # Assemble, shuffle, and send to frontend
    all_choices = [correct_entry] + distractor_entries
    rng.shuffle(all_choices)
    data["params"]["choices"] = all_choices

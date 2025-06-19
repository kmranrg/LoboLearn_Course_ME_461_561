import random

def generate(data):
    seed = data.get("seed")
    rng = random.Random(seed)

    correct = r"Dendrite → Cell body → Axon → Synaptic terminals"

    distractors = [
        r"Synaptic terminals → Axon → Cell body → Dendrite",
        r"Axon → Cell body → Dendrite → Synaptic terminals",
        r"Cell body → Dendrite → Synaptic terminals → Axon",
    ]

    chosen_wrong = rng.sample(distractors, 2)  # pick 2 wrongs

    all_choices = [{"text": correct, "correct": True}] + \
                  [{"text": w, "correct": False} for w in chosen_wrong]
    rng.shuffle(all_choices)

    data["params"]["choices"] = all_choices

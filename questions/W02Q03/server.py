import random

def generate(data):
    """
    Show exactly two options: the true second-derivative test statement,
    plus one random false statement out of the three remaining.
    """

    seed = data.get("seed")
    rng  = random.Random(seed)

    correct = "x₀ is a strict local minimizer of f."

    wrongs = [
        "x₀ is a global minimizer of f.",
        "x₀ is an inflection point of f.",
        "x₀ is a local maximizer of f."
    ]

    distractor = rng.choice(wrongs)

    choices = [
        {"text": correct,     "correct": True},
        {"text": distractor,  "correct": False},
    ]
    rng.shuffle(choices)

    data["params"]["choices"] = choices

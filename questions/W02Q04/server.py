import random

def generate(data):
    """
    Concept Check #1:  ∂L/∂β₀ = 0 ⇒ sum of residuals = 0.
    We’ll show that correct statement plus one random distractor.
    """
    seed = data.get("seed")
    rng  = random.Random(seed)


    correct = r"\(\displaystyle \sum_{n=1}^N (y_n - \hat y_n) = 0\)"


    wrongs = [
      r"\(\displaystyle \sum_{n=1}^N x_n\,(y_n + \hat y_n) = 0\)",
      r"\(\displaystyle \sum_{n=1}^N (y_n + \hat y_n) = 0\)",
      r"\(\displaystyle \sum_{n=1}^N (y_n + \hat y_n)^2 = 0\)",
    ]


    distractor = rng.choice(wrongs)


    choices = [
      {"text": correct,      "correct": True},
      {"text": distractor,   "correct": False},
    ]
    rng.shuffle(choices)


    data["params"]["choices"] = choices

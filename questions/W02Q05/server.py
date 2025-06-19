import random

def generate(data):
    """
    Concept Check #1:  ∂L/∂β₀ = 0 ⇒ sum of residuals = 0.
    We’ll show that correct statement plus one random distractor.
    """
    seed = data.get("seed")
    rng  = random.Random(seed)


    correct = r"\(\displaystyle \hat{\beta}_1 = \frac{\sum_{n=1}^N (x_n - \bar{x}) \, (y_n - \bar{y})}{\sum_{n=1}^N (x_n - \bar{x})^2} \)"


    wrongs = [
      r"\(\displaystyle \hat{\beta}_1 = \frac{\sum_{n=10}^N (x_n - \bar{x}) \, (y_n - \bar{y})}{\sum_{n=1}^N (x_n - \bar{x})^2} \)",
      r"\(\displaystyle \hat{\beta}_1 = \frac{\sum_{n=1}^N (x_n - \bar{x}) \, (y_n + \bar{y})}{\sum_{n=1}^N (x_n - \bar{x})^2} \)",
      r"\(\displaystyle \hat{\beta}_1 = \frac{\sum_{n=1}^N (x_n + \bar{x}) \, (y_n - \bar{y})}{\sum_{n=1}^N (x_n + \bar{x})^2} \)",
    ]


    distractor = rng.choice(wrongs)


    choices = [
      {"text": correct,      "correct": True},
      {"text": distractor,   "correct": False},
    ]
    rng.shuffle(choices)


    data["params"]["choices"] = choices

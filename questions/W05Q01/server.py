import random
import math

def generate(data):
    rng = random.Random(data.get("variant_seed", 5101))

    # Random 2-D weight vector (avoid very small norm)
    w1 = rng.choice([-4, -3, -2, 2, 3, 4])
    w2 = rng.choice([-4, -3, -2, 2, 3, 4])

    # Random bias
    b  = rng.randint(-6, 6)

    # Random test point
    x1 = rng.randint(-6, 6)
    x2 = rng.randint(-6, 6)

    # Compute distance
    numerator   = abs(w1 * x1 + w2 * x2 + b)
    denominator = math.sqrt(w1**2 + w2**2)
    dist        = round(numerator / denominator, 3)

    # Pass parameters to front-end
    data["params"]["w1"] = w1
    data["params"]["w2"] = w2
    data["params"]["b"]  = b
    data["params"]["x1"] = x1
    data["params"]["x2"] = x2

    # Correct numerical answer
    data["correct_answers"]["dist"] = dist

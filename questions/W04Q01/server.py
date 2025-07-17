import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 12345))

    # Random 3D input vector x
    x1 = rng.randint(-3, 3)
    x2 = rng.randint(-3, 3)
    x3 = rng.randint(-3, 3)

    # Random weights w and bias b (ensure non-zero weights)
    def nonzero(): return rng.choice([-3, -2, -1, 1, 2, 3])

    w1 = nonzero()
    w2 = nonzero()
    w3 = nonzero()
    b = rng.randint(-3, 3)

    # Compute perceptron decision
    h = w1 * x1 + w2 * x2 + w3 * x3 + b
    yhat = 1 if h >= 0 else -1

    # Send variables to frontend
    data["params"]["x1"] = x1
    data["params"]["x2"] = x2
    data["params"]["x3"] = x3

    data["params"]["w1"] = w1
    data["params"]["w2"] = w2
    data["params"]["w3"] = w3

    data["params"]["b"] = b

    data["correct_answers"]["yhat"] = yhat

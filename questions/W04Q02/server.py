import random
import math

def generate(data):
    # Random input values for x and weights
    x1 = random.randint(-5, 5)
    x2 = random.randint(-5, 5)
    x3 = random.randint(-5, 5)

    w1 = random.randint(-3, 3)
    w2 = random.randint(-3, 3)
    w3 = random.randint(-3, 3)

    b = random.randint(-2, 2)

    # Compute z = w·x + b
    z = w1 * x1 + w2 * x2 + w3 * x3 + b

    # Sigmoid function
    p = 1 / (1 + math.exp(-z))

    # Binary prediction based on threshold 0.5
    yhat = 1 if p >= 0.5 else 0

    # Pass values to client
    data["params"]["x1"] = x1
    data["params"]["x2"] = x2
    data["params"]["x3"] = x3
    data["params"]["w1"] = w1
    data["params"]["w2"] = w2
    data["params"]["w3"] = w3
    data["params"]["b"] = b

    # Set correct answer
    data["correct_answers"]["yhat"] = yhat

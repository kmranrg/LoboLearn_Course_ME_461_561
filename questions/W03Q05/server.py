import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 3035))

    correct = (
        "Generate noisy data from a known function → define a network with ReLU activations → "
        "train it by minimizing loss → predict using the trained model → visualize predictions vs. true data."
    )

    distractors = [
        "Train the model first → then define your network → finally generate your training data.",
        "Define a neural network without loss or activation → visualize predictions before training.",
        "Predict outputs using random weights → then tune the network until it perfectly matches all data points."
    ]

    choices = [{"text": correct, "correct": True}] + \
              [{"text": d, "correct": False} for d in rng.sample(distractors, 2)]
    rng.shuffle(choices)

    data["params"]["choices"] = choices

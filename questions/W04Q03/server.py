import random

def generate(data):
    rng = random.Random(data.get("variant_seed", 1234))

    correct = "To extract local patterns such as edges, curves, and textures from the input image."

    distractors = [
        "To convert the image into a binary format for easier classification.",
        "To flatten the image into a 1D vector before feeding it into dense layers.",
        "To compute the exact pixel-wise differences between images for comparison."
    ]

    choices = [{"text": correct, "correct": True}] + \
              [{"text": d, "correct": False} for d in rng.sample(distractors, 2)]
    rng.shuffle(choices)

    data["params"]["choices"] = choices

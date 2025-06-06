import random

def generate(data):
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    answer = a * b

    # storing parameters and the correct answer
    data["params"]["a"] = a
    data["params"]["b"] = b
    data["correct_answers"]["answer"] = answer

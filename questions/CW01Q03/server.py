import random

def generate(data):
    b = random.randint(1, 5)
    a_dot_b = random.randint(5, 10)
    a = a_dot_b / b

    # storing parameters and the correct answer
    data["params"]["b"] = b
    data["params"]["a_dot_b"] = a_dot_b
    data["correct_answers"]["a"] = a
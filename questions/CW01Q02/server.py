import random

def generate(data):
    a = random.randint(-6, -1)
    a_dot_b = random.randint(5, 10)
    b = a_dot_b / a

    # storing parameters and the correct answer
    data["params"]["a"] = a
    data["params"]["a_dot_b"] = a_dot_b
    data["correct_answers"]["b"] = b
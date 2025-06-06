import random

def generate(data):
    a1 = random.randint(1, 5)
    a2 = random.randint(-5, 5)
    a3 = random.randint(-5, 5)
    b2 = random.randint(-5, 5)
    b3 = random.randint(5, 10)
    a_dot_b = random.randint(1, 5)
    
    b1 = (a_dot_b - (a2 * b2) - (a3 * b3)) / a1
    
    data["params"]["a1"] = a1
    data["params"]["a2"] = a2
    data["params"]["a3"] = a3
    data["params"]["b2"] = b2
    data["params"]["b3"] = b3
    data["params"]["a_dot_b"] = a_dot_b
    data["correct_answers"]["b1"] = b1
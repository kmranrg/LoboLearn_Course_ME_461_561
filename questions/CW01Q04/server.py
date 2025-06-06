import random

def generate(data):
    a1 = random.randint(1, 5)
    a2 = random.randint(-5, 5)
    b1 = random.randint(1, 5)
    b2 = random.randint(-5, 5)
    
    dot_product = a1 * b1 + a2 * b2
    
    data["params"]["a1"] = a1
    data["params"]["a2"] = a2
    data["params"]["b1"] = b1
    data["params"]["b2"] = b2
    data["correct_answers"]["dot_product"] = dot_product
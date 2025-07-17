import random

def generate(data):
    """
    Q: f(x) = a x^2 + b x,  a ∈ 2ℤ, b ∈ 4ℤ  ⇒  x* = –b/(2a) is always integer.
    Generate random a, x*, compute b so x* is integer, then build 4 MCQ options.
    """

    seed = data.get("seed")
    rng  = random.Random(seed)

    a   = rng.choice([2, 4, 6, 8, 10])
    x0  = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

    b   = -2 * a * x0  
    
    if b < 0:
        b_sign = "-"
        b_val  = abs(b)
    else:
        b_sign = "+"
        b_val  = b

    pool = [i for i in range(-6, 7) if i != x0]
    distractors = rng.sample(pool, 3)
    options     = [x0] + distractors
    rng.shuffle(options)


    choices = []
    for opt in options:
        choices.append({
            "x":       opt,
            "correct": (opt == x0)
        })


    data["params"].update({
        "a":       a,
        "b_sign":  b_sign,
        "b_val":   b_val,
        "choices": choices,
    })


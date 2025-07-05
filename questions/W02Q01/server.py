import random

def generate(data):
    """Simple 'cheapest ride' question with four transport modes."""

    rng   = random.Random(data.get("seed"))  

    # Fixed set of modes
    modes = ["Taxi", "Bus", "Bike", "Scooter"]

    # Random time (min) and money ($) for each mode
    time_ranges  = [(15, 35), (25, 45), (40, 80), (10, 25)]
    money_ranges = [( 5, 15), ( 2,  5), ( 0,  1), ( 3,  8)]

    times  = [rng.randint(*r) for r in time_ranges]
    money  = [rng.randint(*r) for r in money_ranges]

    # Random weights
    w1 = rng.randint(1, 5)      # time weight
    w2 = rng.randint(10, 40)    # money weight

    # Compute cost for each mode and the minimum
    costs = [w1 * t + w2 * m for t, m in zip(times, money)]
    min_cost = min(costs)

    # Pass data to HTML
    for i, m in enumerate(modes):
        data["params"][f"mode{i}"]  = m
        data["params"][f"time{i}"]  = times[i]
        data["params"][f"money{i}"] = money[i]

    data["params"]["w1"] = w1
    data["params"]["w2"] = w2

    # Correct answer
    data["correct_answers"]["answer"] = min_cost

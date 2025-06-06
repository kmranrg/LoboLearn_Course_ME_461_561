# server.py

import random

def generate(data):
    cases = [
        {
            "scenario": "A self-driving drone improves its landing precision by trying different approaches and learning from the reward it receives for soft landings.",
            "correct": "Reinforcement Learning",
            "image" : "drone.png"
        },
        {
            "scenario": "A satellite image classifier is trained using labeled images to detect whether an image contains a cloud or not.",
            "correct": "Supervised Learning",
            "image" : "satellite.png"
        },
        {
            "scenario": "A system groups similar aircraft engine vibration patterns without knowing what each group means beforehand.",
            "correct": "Unsupervised Learning",
            "image" : "aircraft.png"
        },
        {
            "scenario": "A Mars rover improves its navigation by exploring terrain and receiving feedback based on safe travel.",
            "correct": "Reinforcement Learning",
            "image" : "rover.png"
        },
        {
            "scenario": "A weather model is trained using years of past labeled data to predict temperature from humidity and pressure.",
            "correct": "Supervised Learning",
            "image" : "weather.png"
        },
        {
            "scenario": "An algorithm clusters thousands of aircraft flight trajectories based on similarity without knowing what each group means.",
            "correct": "Unsupervised Learning",
            "image" : "algorithm.png"
        }
    ]

    case = random.choice(cases)
    data["params"]["scenario"] = case["scenario"]
    data["params"]["image"] = case["image"]
    data["params"]["is_SL"] = str(case["correct"] == "Supervised Learning").lower()
    data["params"]["is_UL"] = str(case["correct"] == "Unsupervised Learning").lower()
    data["params"]["is_RL"] = str(case["correct"] == "Reinforcement Learning").lower()

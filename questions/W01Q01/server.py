import random


def generate(data):
    # -----------------------
    # 1.  Three worked-out cases
    # -----------------------
    cases = [
        {
            "scenario": (
                "An email filter gets better at spotting spam after it sees "
                "thousands of labelled emails."
            ),
            "T": "classify incoming emails as spam or not-spam",
            "P": "classification accuracy (higher is better)",
            "E": "previously labelled emails",
        },
        {
            "scenario": (
                "A robot quad-rotor gradually improves its landing by trying "
                "hundreds of landings and measuring its touchdown velocity."
            ),
            "T": "execute a smooth landing",
            "P": "average touchdown velocity (lower is better)",
            "E": "past landing attempts",
        },
        {
            "scenario": (
                "A movie recommender suggests films after observing what "
                "ratings similar users give."
            ),
            "T": "suggest a movie the user will like",
            "P": "mean squared error between predicted and actual ratings",
            "E": "user–movie rating history",
        },
        {
            "scenario": (
                "A self-driving car learns to navigate intersections more smoothly "
                "after being exposed to thousands of driving scenarios in simulation."
            ),
            "T": "navigate intersections safely and smoothly",
            "P": "number of abrupt stops or collisions",
            "E": "simulated driving experiences",
        },
        {
            "scenario": (
                "A medical diagnosis model learns to detect diabetic retinopathy "
                "from patient eye scans by training on past labeled images."
            ),
            "T": "identify signs of diabetic retinopathy in eye scans",
            "P": "diagnostic accuracy compared to expert evaluation",
            "E": "labeled eye scan images from past patients",
        },
        {
            "scenario": (
                "An intelligent tutoring system improves its lesson recommendations "
                "after analyzing student quiz performance over time."
            ),
            "T": "recommend personalized lessons to students",
            "P": "quiz score improvement after recommendation",
            "E": "student quiz performance history",
        },
    ]


    case = random.choice(cases)

    # -----------------------
    # 2.  Build & shuffle the three (statement, label) pairs
    # -----------------------
    items = [
        (case["T"], "T"),
        (case["P"], "P"),
        (case["E"], "E"),
    ]
    random.shuffle(items)

    statements = [text for text, _ in items]
    labels     = [lbl  for _, lbl  in items]

    # -----------------------
    # 3.  Pass everything to PrairieLearn
    # -----------------------
    data["params"]["scenario"] = case["scenario"]

    for i, (stmt, lbl) in enumerate(zip(statements, labels)):
        data["params"][f"statement{i}"] = stmt
    
        data["params"][f"lab{i}_is_T"] = "true"  if lbl == "T" else "false"
        data["params"][f"lab{i}_is_P"] = "true"  if lbl == "P" else "false"
        data["params"][f"lab{i}_is_E"] = "true"  if lbl == "E" else "false"


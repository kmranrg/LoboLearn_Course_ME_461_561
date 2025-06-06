import random

def generate(data):
    # --- canonical lists ----------------------------------------------------
    skills = [
        "Mathematics",
        "Programming skills",
        "Computer and data literacy",
        "ML algorithms",
        "Critical thinking",
    ]

    tools = ["Python", "Jupyter Notebook", "Tensorflow"]

    # pick ONE random word (either a skill or a tool, never both)
    if random.choice([True, False]):                # True ⇒ pick a skill
        word  = random.choice(skills)
        label = "Skill"
    else:                                           # False ⇒ pick a tool
        word  = random.choice(tools)
        label = "Tool"

    # put into params so HTML can render / grade
    data["params"]["word"] = word
    data["params"]["skillAttr"] = "true" if label == "Skill" else "false"
    data["params"]["toolAttr"]  = "true" if label == "Tool"  else "false"

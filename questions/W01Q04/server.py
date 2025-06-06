import random

def generate(data):
    # Full pool of possible statements
    statements = [
        {
            "text": "You need a Google account to use Google Colab.",
            "correct": True
        },
        {
            "text": "Google Colab runs entirely in your web browser without needing local installation.",
            "correct": True
        },
        {
            "text": "You must install Jupyter Notebook to use Google Colab.",
            "correct": False
        },
        {
            "text": "Google Colab cannot run code that uses NumPy.",
            "correct": False
        },
        {
            "text": "You can create and run Python notebooks directly at https://colab.research.google.com.",
            "correct": True
        }
    ]

    # Pick 3 random statements
    selected = random.sample(statements, 3)

    # Store in params for rendering in question.html
    for i, stmt in enumerate(selected):
        data["params"][f"text{i}"] = stmt["text"]
        data["params"][f"correct{i}"] = stmt["correct"]

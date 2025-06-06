import random

def generate(data):
    jupyter_statements = [
        {
            "text": "You can install Jupyter Notebook locally by installing the Anaconda distribution.",
            "correct": True
        },
        {
            "text": "Jupyter Notebook can be launched from Anaconda Navigator.",
            "correct": True
        },
        {
            "text": "To install Jupyter Notebook with pip, you can run: pip install notebook.",
            "correct": True
        },
        {
            "text": "Jupyter Notebook only works on macOS, not Windows.",
            "correct": False
        },
        {
            "text": "Jupyter Notebook opens in your browser after launching it from terminal or Anaconda Navigator.",
            "correct": True
        },
        {
            "text": "You need a Google account to run Jupyter Notebook locally.",
            "correct": False
        }
    ]

    selected = random.sample(jupyter_statements, 3)

    for i, stmt in enumerate(selected):
        data["params"][f"text{i}"] = stmt["text"]
        data["params"][f"correct{i}"] = stmt["correct"]

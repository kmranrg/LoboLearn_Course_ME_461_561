import random
import math
import numpy as np

def sigmoid(value):
    result = 1 / (1 + math.exp(-value))
    return result

def generate(data):
    A = np.array([[random.randint(-5, 10)] for _ in range(10)], dtype=float)

    Y = A.copy()
    row, column = Y.shape
    for r in range(row):
        for c in range(column):
            Y[r][c] = round(sigmoid(A[r][c]),4)

    answer = Y[0,0]

    # storing parameters and the correct answer
    row, column = A.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"A{r}{c}"] = A[r][c]

    row, column = Y.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"Y{r}{c}"] = round(Y[r][c],4)

    data["correct_answers"]["answer"] = round(answer,4)
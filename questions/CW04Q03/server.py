import random
import numpy as np

def ReLU(value):
    if value <= 0:
        return 0
    else:
        return value

def generate(data):
    A = np.array([[random.randint(-5, 5)],
                  [random.randint(-5, 5)],
                  [random.randint(-5, 5)],
                  [random.randint(-5, 5)],
                  [random.randint(-5, 5)],
                  [random.randint(-5, 5)],
                  [random.randint(-5, 5)],
                  [random.randint(-5, 5)],
                  [random.randint(-5, 5)],
                  [random.randint(-5, 5)]])

    Y = A.copy()
    row, column = Y.shape
    for r in range(row):
        for c in range(column):
            Y[r][c] = ReLU(A[r][c])

    answer = Y[0,0]

    # storing parameters and the correct answer
    row, column = A.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"A{r}{c}"] = int(A[r][c])

    row, column = Y.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"Y{r}{c}"] = int(Y[r][c])

    data["correct_answers"]["answer"] = int(answer)
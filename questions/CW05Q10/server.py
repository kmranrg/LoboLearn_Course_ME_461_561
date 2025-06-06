import random
import numpy as np

def ReLU(value):
    if value <= 0:
        return 0
    else:
        return value

def generate(data):
    X = np.array([[random.randint(-5, 5)],
                  [random.randint(-5, 5)],
                  [1]])
    Wb = np.array([[random.randint(1, 5), random.randint(-5, 5), random.randint(-5, 5)],
                   [random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)],
                   [random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)]])
    H = np.dot(Wb, X)

    Y = H.copy()
    row, column = Y.shape
    for r in range(row):
        for c in range(column):
            Y[r][c] = ReLU(H[r][c])

    answer = X[0,0]

    # storing parameters and the correct answer
    row, column = X.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"X{r}{c}"] = int(X[r][c])
    
    row, column = Wb.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"Wb{r}{c}"] = int(Wb[r][c])

    row, column = H.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"H{r}{c}"] = int(H[r][c])

    row, column = Y.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"Y{r}{c}"] = int(Y[r][c])

    data["correct_answers"]["answer"] = int(answer)
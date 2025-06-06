import random
import numpy as np
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def generate(data):
    X = np.array([[random.randint(-5, 5)],
                  [random.randint(-5, 5)],
                  [1]])
    Wb = np.array([[random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)]])
    H = np.dot(Wb, X)

    Y = H.copy()
    row, column = Y.shape
    for r in range(row):
        for c in range(column):
            Y[r][c] = round(sigmoid(H[r][c]))

    first_answer = H[0,0]
    second_answer = float(Y[0,0])

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
            data["params"][f"Y{r}{c}"] = float(Y[r][c])

    data["correct_answers"]["answer1"] = int(first_answer)
    data["correct_answers"]["answer2"] = int(second_answer)
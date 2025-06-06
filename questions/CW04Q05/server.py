import random
import numpy as np
import math

def sigmoid(value):
    return 1 / (1 + math.exp(-value))

def generate(data):
    X = np.array([[random.randint(-5, 5)],
                  [random.randint(-5, 5)],
                  [1]], dtype=int)   
    Wb = np.array([[random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)],
                   [random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)],
                   [random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)]], dtype=int)   

    H = np.dot(Wb, X)

    Y = H.copy()
    row, column = Y.shape
    for r in range(row):
        for c in range(column):
            Y[r][c] = round(sigmoid(Y[r][c]), 4) 

    answer = Y[2, 0]

    # Now safe to store into `data`
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

    data["correct_answers"]["answer"] = float(answer)

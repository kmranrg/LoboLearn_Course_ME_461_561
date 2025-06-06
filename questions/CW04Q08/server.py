import random
import math
import numpy as np

def sigmoid(value):
    return 1 / (1 + math.exp(-value))
    
def tanh(value):
    return math.tanh(value)

def generate(data):
    A = np.array([[random.randint(-10, 10)] for _ in range(10)], dtype=float)

    Y = A.copy()
    row, column = Y.shape
    for r in range(row):
        for c in range(column):
            Y[r][c] = round(tanh(A[r][c]),4)
    
    Z = Y.copy()
    row, column = Y.shape
    for r in range(row):
        for c in range(column):
            Z[r][c] = round(sigmoid(Y[r][c]),4)
            
    answer = Z[0,0]

    # storing parameters and the correct answer
    row, column = A.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"A{r}{c}"] = A[r][c]

    row, column = Y.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"Y{r}{c}"] = round(Y[r][c],4)
            
    row, column = Z.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"Z{r}{c}"] = round(Z[r][c],4)

    data["correct_answers"]["answer"] = round(answer,4)
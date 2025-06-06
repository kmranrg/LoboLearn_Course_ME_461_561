import random
import numpy as np

def generate(data):
    X = np.array([[random.randint(1, 5)],
                  [random.randint(-5, 5)],
                  [random.randint(-5, 5)],
                  [1]])
    Wb = np.array([[random.randint(1, 5), random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)],
                   [random.randint(1, 5), random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)]])
    Y = np.dot(Wb, X)
    answer = Y[1,0]

    # storing parameters and the correct answer
    row, column = X.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"X{r}{c}"] = int(X[r][c])
    
    row, column = Wb.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"Wb{r}{c}"] = int(Wb[r][c])

    row, column = Y.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"Y{r}{c}"] = int(Y[r][c])

    data["correct_answers"]["answer"] = int(answer)
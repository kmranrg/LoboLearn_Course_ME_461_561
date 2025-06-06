import random
import numpy as np

def generate(data):
    A = np.array([[random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)],
                  [random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)]])
    B = np.array([[random.randint(-10, 10), random.randint(-10, 10)],
                  [random.randint(-10, 10), random.randint(-10, 10)],
                  [random.randint(-10, 10), random.randint(-10, 10)],
                  [random.randint(-10, 10), random.randint(-10, 10)]])
    BA = np.dot(B, A)
    answer = BA[2,2]

    # storing parameters and the correct answer
    row, column = A.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"A{r}{c}"] = int(A[r][c])
    
    row, column = B.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"B{r}{c}"] = int(B[r][c])

    row, column = BA.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"BA{r}{c}"] = int(BA[r][c])

    data["correct_answers"]["answer"] = int(answer)
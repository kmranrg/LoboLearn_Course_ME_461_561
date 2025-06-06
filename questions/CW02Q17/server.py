import random
import numpy as np

def generate(data):
    A = np.array([[random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)],
                  [random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)],
                  [random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)],
                  [random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)]])
    B = np.array([[random.randint(-10, 10), random.randint(-10, 10)],
                  [random.randint(-10, 10), random.randint(-10, 10)],
                  [random.randint(-10, 10), random.randint(-10, 10)],
                  [random.randint(-10, 10), random.randint(-10, 10)]])
    AB = np.dot(A, B)
    answer = AB[1,1]

    # storing parameters and the correct answer
    row, column = A.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"A{r}{c}"] = int(A[r][c])
    
    row, column = B.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"B{r}{c}"] = int(B[r][c])

    row, column = AB.shape
    for r in range(row):
        for c in range(column):
            data["params"][f"AB{r}{c}"] = int(AB[r][c])

    data["correct_answers"]["answer"] = int(answer)
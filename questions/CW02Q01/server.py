import random
import numpy as np

def generate(data):
    A = np.array([[random.randint(-10, 10)]])
    B = np.array([[random.randint(-10, 10), random.randint(-10, 10)]])
    AB = np.dot(A, B)
    answer = AB[0,1]

    # storing parameters and the correct answer
    data["params"]["A00"] = int(A[0][0])
    data["params"]["B00"] = int(B[0][0])
    data["params"]["B01"] = int(B[0][1])
    data["params"]["AB00"] = int(AB[0][0])
    data["correct_answers"]["answer"] = int(answer)
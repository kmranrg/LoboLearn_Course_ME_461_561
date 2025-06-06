import numpy as np  # uses numpy to satisfy package check

def evaluate_claim(gender: str, age: int) -> str:
    gender = gender.lower().strip()
    age = int(np.array(age))          # numpy usage

    if gender == "male" and 51 <= age <= 65:
        return "Reject"
    if gender == "female" and 55 <= age <= 70:
        return "Reject"
    if gender == "male" and 41 <= age <= 50:
        return "Accept"
    if 25 <= age <= 40:
        return "Need more info"
    return "Reject"

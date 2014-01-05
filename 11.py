lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(lst):
    sum = 0
    for grade in lst:
        sum += grade
    average = float(sum) / len(lst)
    return average

def get_average(student):
    return .1 * average(student["homework"]) + .3 * average(student["quizzes"]) + .6 * average(student["tests"])
    
def get_letter_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    elif score < 60: return "F"
    
def get_class_average(class_list):
    sum = 0
    for student in class_list:
        sum += get_average(student)
    return float(sum) / len(class_list)
    
print get_letter_grade(get_average(lloyd))

#Code for codecademy.com Lesson 16
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(to_print):
    for grade in grades:
        print grade
print_grades(grades)

def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total

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

def grades_average(scores):
    to_return = float(grades_sum(scores)) / float(len(scores))
    return to_return

def grades_variance(scores, average):
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    variance /= len(scores)
    return variance

def grades_std_deviation(variance):
    return sqrt(variance)

print "All grades ", grades
print "Sum of grades ", grades_sum(grades)
print "Average grades ", grades_average(grades)
print "Variance ", grades_variance(grades, grades_average(grades))
print "Standard deviation ", grades_std_deviation(grades_variance(grades, grades_average(grades)))

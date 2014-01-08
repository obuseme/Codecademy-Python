# Lesson 15 from Python course at codecademy.com

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def is_int(x):
    rounded_x = round(x)
    if rounded_x - x == 0:
        return True
    else:
        return False

def digit_sum(n):
    string_n = str(n)
    sum = 0
    for i in string_n:
        print "i=" + i
        sum += int(i)
    return sum

def factorial(x):
    to_return = 1
    if x == 0:
        return 0
    while x > 0:
        to_return *= x
        x -= 1
    return to_return

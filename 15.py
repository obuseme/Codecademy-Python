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

def is_prime(x):
    if x < 2:
        return False
    to_check = x - 1
    while to_check > 1:
        if x % to_check == 0:
            return False
        to_check -= 1
    return True

def reverse(text):
    to_return = ""
    for n in range(len(text)):
        print to_return
        to_return += text[len(text)-n - 1]
    return to_return

def anti_vowel(text):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    to_return = ""
    for n in text:
        if n not in vowels:
            to_return += n
    return to_return

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
def scrabble_score(word):
    word = word.lower()
    score_to_return = 0
    for letter in word:
        score_to_return += score[letter]
    return score_to_return

def censor(text, word):
    filler = ""
    for letter in word:
        filler += "*"
    text = text.replace(word, filler)
    return text

def count(sequence, item):
    count = 0
    for something in sequence:
        if something == item:
            count += 1
    return count

def purify(numbers):
    new_list = []
    for number in numbers:
        if number % 2 == 0:
            new_list.append(number)
    return new_list

def product(integers):
    to_return = 1
    for number in integers:
        to_return *= number
    return to_return

def remove_duplicates(to_check):
    to_return = []
    for something in to_check:
        if something not in to_return:
            to_return.append(something)
    return to_return

def median(to_check):
    to_check = sorted(to_check)
    if len(to_check) == 1:
        return to_check[0]
    if len(to_check) % 2 == 0:
        half_len = len(to_check) / 2
        return (to_check[half_len] + to_check[half_len-1]) / 2.0
    else:
        return to_check[len(to_check)/2]

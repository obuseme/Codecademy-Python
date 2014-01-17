# Code for Python Lesson 18 in codecademy.com

one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

print bin(1)
print bin(2)
print bin(3)
print bin(4)
print bin(5)

prinnt("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
print int("11001001",2)

hift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_left = shift_left << 2
shift_right = shift_right >> 2

print bin(shift_right)
print bin(shift_left)

print bin(0b1110 & 0b101)

print bin(0b1110 | 0b101)

# XOR
print bin(0b1110 ^ 0b101)

#NOT operator (and 1 and then multiply by -1)
print ~1
print ~2
print ~3
print ~42
print ~123

def check_bit4(to_check):
    result = int(to_check & 0b1000)
    if result > 0:
        return "on"
    else:
        return "off"

a = 0b10111011
a = a | 0b100
print bin(a)

a = 0b11101110
print(bin(a ^ 0b11111111))

def flip_bit(number, n):
    mask = 0b1 << (n - 1)
    desired = number ^ mask
    return bin(desired)


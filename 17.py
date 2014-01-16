#Code for Lesson 17

my_dict = {"Name": "Andy", "Instrument":"Guitar"}
print my_dict.items()
for key in my_dict:
	print key

even_squares = [x**2 for x in range(1,11) if x**2%2 == 0]
cubes_by_four = [x**3 for x in range(1,11) if x**3%4==0]

my_list = range(1, 11) # List of numbers 1 - 10
print my_list[::2]

my_list = range(1, 11)
backwards = my_list[::-1]

to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

to_21 = [x for x in range(1,22)]
odds = to_21[::2]
middle_third = to_21[7:14:1]

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

nguages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)

# prints squares of numbers 1 through 10, that are between 30 and 70 inclusive
squares = [x**2 for x in range(1, 11)]
print filter(lambda x: x >= 30 and x <= 70, squares)

movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}

print movies.items()

threes_and_fives = [x for x in range(1,16) if x%3==0 or x%5==0]

# decode the secret message
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print message




## Practice Typing code
## Learning Python 3 the Hardway
## Exercise 6

# Defines types of people variable
types_of_people = 10
#  Assigns string with formating to x, var is inserted as part of formating
#                   String in string
x = f"There are {types_of_people} types of people."

# Defines variable as string
binary = "binary"
# String defined as variable
do_not = "don't"
# y is defined as formated string with vars inserted in {}
#                   String in string
y = f"Those who know {binary} and those who {do_not}."

# prints x and y strings with formating and vars
print(x)
print(y)

# Adds new string to prev x/y string with var/formating
# String in string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# defines bools and string with empty set
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# prints joke_eval, empty set is filled with False
print(joke_evaluation.format(hilarious))
# Defines new strings
w = "This is the left side of..."
e = "a string with a right side."
# prints contenations of w and e
# + behaves like contenations as this is the equivalent for strings
print(w + e)

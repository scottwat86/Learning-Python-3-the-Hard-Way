## Practice Typing code
## Learning Python 3 the Hardway
## Exercise 8


# creates a series of empty "{}" inside a string var
formatter = "{} {} {} {}"


# that format() takes tuple and cannot be outside the range of {} to replace
# calls format function to replace {} with int 1, 2, 3, 4
print(formatter.format(1, 2, 3, 4))
# calls format function to replace {} with string one, two...
print(formatter.format("one", "two", "three", "four"))
# calls format function to replace {} with boolean
print(formatter.format(True, False, False, True))
# calls format function to replace {} with itself (a string)
print(formatter.format(formatter, formatter, formatter, formatter))
# calls format function to replace {} with a series of strings
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

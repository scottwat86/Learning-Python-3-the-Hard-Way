## Practice Typing code
## Learning Python 3 the Hardway
## Exercise 7 - More Printing

# prints string
print("Mary had a little lamb.")
# prints string with {} filled in by format input string
print("Its fleece was white as {}.".format('snow'))
# prints string
print("And everywhere that Mary went.")
# prints 10 periods
print("." * 10) # what'd that do?

# Defines a series of letters
end1  = "C"
end2  = "h"
end3  = "e"
end4  = "e"
end5  = "s"
end6  = "e"
end7  = "B"
end8  = "u"
end9  = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
# The end=' ' makes the end of print a space instead of \n
# This makes the next print on the same line
# Assembles the letters into a string
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

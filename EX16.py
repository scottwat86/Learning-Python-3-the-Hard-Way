## Practice Typing code
## Learning Python 3 the Hardway
## Exercise 16 - Reading and Writing Files

# imports argv from sys module
from sys import argv

# Takes in argument file name
script, filename = argv

# Inserts the file name from argv into string
print(f"We're going to erase {filename}.")
# confirms from the user that they indeed want to delete the file contents
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")
""" No conditional is need to check the user input b/c the
user prompt above directs the user to exit the py or continue
"""
print("Opening the file . . . ")
# Opens the file and assigns to target var
# 'w' mode allows writing, truncating file first
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# deletes contents of file before beginning
target.truncate()

print("Now I'm going to ask you for three lines.")

#  Takes three lines from user

# line1 = input("line 1: ")
# line2 = input("line 2: ")
# line3 = input("line 3: ")

# print("I'm going to write there to the file.")

# writes var to file with new lines per entry
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# creates an empty list
# Only downside is this hard codes 3 lines to enter
# For loop appends list with input and then writes to file
lines = []
for i in range(3):
    lines.append(input(f"line {i+1}: "))
    target.write(lines[i] + '\n')

print("And finally, we close it.")
#closes file
target.close()

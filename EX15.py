## Practice Typing code
## Learning Python 3 the Hardway
## Exercise 15

# Imports argv method from sys module
from sys import argv

# Script is the name of the script that is running
# Then takes in an argument and initializes to filename
script, filename = argv

# Opens file and creates file object / instance -> txt of function open()
txt = open(filename)

# Prints the file name var along with string
print(f"Here's your file {filename}:")
# reads instance of open to Print
print(txt.read())
txt.close()

# Prints string
print("Type the filename again:")
# Takes input and reassigns to filename to open
file_again = input("> ")

# Opens new file after input
txt_again = open(file_again)

# reads file and prints
print(txt_again.read())
txt_again.close()

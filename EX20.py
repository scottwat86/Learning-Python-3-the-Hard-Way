## Practice Typing code
## Learning Python 3 the Hardway
## Exercise 20 - Functions and Files

# Imports argv from sys module
from sys import argv

# takes in argument from prompt at run and initializes input_ file var for file name
script, input_file = argv

# defines print all function. Uses
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

# opens the file and assigned instance to current_file, "r+" reading and updating
current_file = open(input_file, "r+")

# writes three lines to the file
current_file.write("The cat in the hat.\n")
current_file.write("This is line 2.\n")
current_file.write("This is line 3.\n")
# need this or else there isn't anything to print in the file later
# on the next print
rewind(current_file)

# Intro string
print("First let's print the whole file:\n")

# calls print_all() function
print_all(current_file)

# intro string
print("Now let's rewind, kind of like a tape.")

# Calls rewind function -> uses seek to go to beginning of file
rewind(current_file)

# Intro
print("Let's print three lines:\n")

# Prints the first line
current_line = 1
print_a_line(current_line, current_file)

# Prints the second line
current_line += current_line
print_a_line(current_line, current_file)

#Prints third line
current_line += current_line
print_a_line(current_line, current_file)

# I added close the file
current_file.close()

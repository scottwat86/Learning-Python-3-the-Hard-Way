## Practice Typing code
## Learning Python 3 the Hardway
## Exercise 22

# This is a single line comment
'''
This is a
multiline
comment
If this were in a place where a string could be it would be a multiline string
'''

# STRINGS & PRINTING
" The" # string
' The ' # another string
"""
T
H
E
""" # yet another string
'''
T
H
E
''' # also string

"""

\\             BACKSLASH'
\'            SINGLE QUOTE
\"           DOUBLE QUOTE
\a           ASCII BELL
\b          ASCII BACKSPACE
\f          FORMFEED
 \n        NEWLINE
\r          CARRIAGE RETURN
\t          TAB
"""

print("Prints this string to the command prompt.\n")
cars = 100
#Formating
print("There are", cars, "cars"+' in the parking lot.') #There are 100 cars in the parking lot
#+ joins strings   ',' within print will also joint strings
print(f"There are {cars} cars in the parking lot.") # notice the variable in {} prints the same as above
# Initializes variable with string and empty formating set
string_variable = "There are {} cars in the parking lot"
# string calls format function which fills in the empty {} with the var cars
print(string_variable.format(cars))

print("-".join("HAT")) # H-A-T
print("."*10) # ..........
print("The cat", end=" ") #  end= revises ending from \n newline
print("in the hat") # prints "The cat in the har"

#INPUT
var = input("Enter your answer here:\n> ") # prompts user to enter string

# Imports argv argument from sys module
 from sys import argv
 # takes in script name, second, and third strings at the command prompt
  script, second, third = argv
print("File:{script}\nSecond: {second}\nThird: {third}")
# prints name of file currently running and argument second and third

#FILES
# Opens an instance of file, Make sure the path is a string and use \\ to get the path right
# "r" = read (default)        "w" = write mode  "r+" = read / write
# "a" = append file
file_in = open("C:\\Users\\scott_watson\\Documents\\Python\\lpthw\\test.txt", "r+")
file_data = file_in.read() # reads all the file to file_data
file_line = file_in.readline() # reads just a line
file_in.write("String written") # writes string to file where ever the seek is located
########## THIS ISNT WORKING!
# file_in.append("Adds string to the end of file")

# Removes all text from file
file_in.truncate()
print(file_in.read())
file_in.close() # closes the file


# same as above but auto closes file
file_path = "C:\\Users\\scott_watson\\Documents\\Python\\lpthw\\test.txt"
with open(file_path, "r+") as file:
    file_data = file.read()
    file.write("String to be written")
    file.seek(0)  # Sets the place in the file to the beginning
    ########## THIS ISNT WORKING!
    # file.append("Adds string to the end of file")

# imports exists from the os.path module
from os.path import exists
# Exists() takes a string of file name and/or path and checks if the file exists
# TRUE if it exists.
print(exists(file_path))

# DATA TYPEtype() # checks type of input
str() # creates a string from the input
int() # converts input into integer
float() # converts into FLOAT

len([1,2,[3,4]]) #Takes an iterable and returns the # of elements; 3 in this case
# subelement are counts as 1 element hence [3,4] ->1+

formatter = "{} {} {} {}"
formatter.format(1,2,3,4) # input is a tuble and must match quantity

# NUMBERS
2.0 # a float
1   # integer
1+1 # addition
1-1 # subtraction
x += x # takes right side and adds 1 and assigns to left side
x -= x # same as above but subtraction

1*1 # Multiplication
1/2 # Division -> returns a FLOAT
1 // 2 # Floor Division  returns a whole number and trucates decimal
1 % 2 # Modulus returns remainder from division -> 0.5 in this case
2**2 # exponential 2^2

True    # boolean
False  #
and
or
not
in
not in

# The below checks return a boolean TRUE or FALSE
== # equal to
!= # not equal to  -> BANG-EQUALS
< # less than
=< # less than or equal to
> # greater than
=> # greater than or equal to

#FUNCTIONS   METHODS   CLASS
 def function(x): # begins function block with function name and imput arguments
    y = x**2  # conducts calculations or modifies input x
    return y  # return y, if nothing is return this function will return nothing

print(function(3))

#This is a little more advanced than the book!

#  CLASS & SUBCLASS
class person:

        def __init__(self, height, weight, eye_color): # constructor with attributes
            self.height = height
            self.weight = weight
            self.eye_color = eye_color

class family(person):  #  subclass of person

        def __init__(self, height, weight, eye_color, relation):  # constructor
            super().__init__(height, weight, eye_color) # family inheriting person attr
            self.relation = relation # adds relation attr


# individual = person(6.0,170,"brown")
#bob = family(6.0, 170,"brown", "father")
# print(" "+str(individual.height), "ft\n",f"{individual.weight} lb\n",individual.eye_color)
print(" "+str(bob.height), "ft\n",f"{bob.weight} lb\n",bob.eye_color, "he is my", bob.relation)

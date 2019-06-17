## Practice Typing code
## Learning Python 3 the Hardway
## Exercise 13  - Parameters Unpacking Variables


from sys import argv
# read the WYSS section for gow to run thingss
## Takes three user inputs at command line when the scrip is called
script, first, second, third = argv

## Lists the file name of the script
print("The script is called:", script)
## prints Var 1, 2, & 3
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

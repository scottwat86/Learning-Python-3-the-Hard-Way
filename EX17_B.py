## Practice Typing code
## Learning Python 3 the Hardway
## Exercise 17

# Imports argv from sys module
from sys import argv
# imports exists from os.path module
from os.path import exists

# Takes the script.py, and two input files to modify
script, from_file, to_file = argv

# Adds the from_file and to_file to the string
print(f"Copying from {from_file} to {to_file}")

# Original
# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# Revised
# Opens from_file as instance to in_file
# Then reads data into indata and closes from_file
# with open(from_file) as to_file: indata = to_file.read()

# print(f"The input file is {len(indata)} bytes long")

# print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()

out_file = open(to_file, "w")
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

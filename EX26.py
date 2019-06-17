## Practice Typing code
## Learning Python 3 the Hardway
## Exercise 26 Congratulations, Take a Test!

from sys import argv # I think they forgot the import argv statement

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input() # Forgot his entire line
print("How much do you weigh?", end=' ') # Missing )
weight = input()

print(f"So, you're {age} years old, {height} tall, and {weight} heavy.")

script, filename = argv

txt = open(filename) # misspelled filenAme

print(f"Here's your file: {filename}:")  #forgot the f to fill the {var}
print(txt.read()) # misspelled txT
txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read()) # used _ instead of .
txt_again.close() # neither file was closed at the end

print('Let\'s practice everything.') # forgot the \' for the single quote
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.') # can't seperate on lines unless using """ """

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern the needs of love
nor comprehend passion from intuition
and requires an explanation
\twhere there is none.
"""

print("--------------") # Forgot " on either of the prints
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6 # forgot 6
print(f"This should be five: {five}") # Forgot the ) closing

def secret_formula(started): # Forgot :
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars  * 100 #forgot *
    return jelly_beans, jars, crates

start_point = 10_000 # I added the _ to make it clear that its 10,000 NOT 1,000
jelly_beans, jars, crates = secret_formula(start_point) # misspelled jelly beans and forgot crates

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {jelly_beans} jelly beans, {jars} jars, and {crates} crates.") # forgot jelly_

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) # forgot _
# this is an easy way to apply a list to a format string
print("We'd have {} jelly beans, {} jars, and {} crates.".format(*formula))


people = 20
cats = 30 # cats not cates
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!") # forgot ()

if people > cats: # pretty sure they flipped the > to a <
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: # forgot the :
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.") # Forgot " and :

if people == dogs: # need a boolean not an assignment
    print("People are dogs.")

## Practice Typing code
## Learning Python 3 the Hardway
## Exercise 5 - More Variable and Printing

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'


print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")


# this line is tricky, try to get it eactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# I cheated and used search and replace
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# The set brackets contain variable names that are replaced by the var value
# You need f"" for it to work
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")


# this line is tricky, try to get it eactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

#
# inch_to_cm = 2.54 # cm/inch
# lbs_to_kg = 2.2 # kg/lbs
#
# name = 'Zed A. Shaw'
# age = 35 # not a lie
# height = 74 * inch_to_cm  # inchs * cm/inch
# weight = 180 * lbs_to_kg  # lbs * 2.2 kg/lbs
# eyes = 'Blue'
# teeth = 'White'
# hair = 'Brown'
#
# print(f"Let's talk about {name}.")
# print(f"He's {height} inches tall.")
# print(f"He's {weight} pounds heavy.")
# print(f"Actually that's not too heavy.")
# print(f"He's got {eyes} eyes and {hair} hair.")
# print(f"His teeth are usually {teeth} depending on the coffee.")
#
#
# # this line is tricky, try to get it eactly right
# total = age + height + weight
# print(f"If I add {age}, {height}, and {weight} I get {total}.")

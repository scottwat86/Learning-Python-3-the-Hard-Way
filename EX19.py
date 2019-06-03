## Practice Typing code
## Learning Python 3 the Hardway
## Exercise 19
#
# # Defines a function that takes two var inputs
# # Prints the var in several strings
# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     print(f"You have {cheese_count} cheeses!")
#     print(f"You have {boxes_of_crackers} boxes of crackers!")
#     print("Man that's enough for a party!")
#     print("Get a blanket.\n")
#
# # String print
# # calls cheese_and_crackers funtcion with direct inputs of 20/30
# print("We can just give the function numbers directly:")
# cheese_and_crackers(20, 30)
#
# # Same as above but variables are entered as input
# print("OR, we can use variables from our script:")
# amount_of_cheese = 10
# amount_of_crackers = 50
#
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# # Same as above but adds two sets of int before inputing into f(x)
# print("We can even do math inside too:")
# cheese_and_crackers(10 + 20, 5 + 6)
# # Inputs var + int
# print("And we can combine the two, variables and math:")
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)
from math import pi
import random

def cylinder_volume (radius, height):
    volume = pi* radius**2 * height
    return volume

print(cylinder_volume(random.randint(1,10),random.randint(2,20)))

r = 2
h = 10
print(cylinder_volume(r, h))
print(cylinder_volume(2,10))
print(cylinder_volume(1+2,3+7))
print(cylinder_volume(r+1,h))
print(cylinder_volume(2*2,2*2))

r_h = [2,10]
h_r = (2,10)
r__h = {2,10}
print(cylinder_volume(*r_h))
print(cylinder_volume(r_h[0],r_h[1]))
print(cylinder_volume(*h_r))
print(cylinder_volume(*r__h))

r = int(input("Enter the radius:\n> "))
h = int(input("Enter the height:\n> "))
print(cylinder_volume(r,h))

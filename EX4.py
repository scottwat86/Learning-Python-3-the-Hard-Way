## Practice Typing code
## Learning Python 3 the Hardway
## Exercise 4

# Declares variable names
# Integer for cars
cars = 100
# Space in cars is a float
# if you replace 4.0 with 4 the number becomes an Integer
space_in_a_car = 4.0
# drivers is an Integer
drivers = 30
# Passengers is also an Integer
passengers = 90
# Calculates the the number of cars that doesn't have drivers
cars_not_driven = cars - drivers
# Assumes for every driver there is a car to drive
cars_driven = drivers
# Calculates the carpooling capacity based on # of cars driven and space in cars
carpool_capacity = cars_driven * space_in_a_car
# Averages the passengers per car driven
# ERROR The first pass added an '_' to the name and python does not
# see carpool_capacity == car_pool_capacity to be the same
# because _ is part of the name
average_passengers_per_car = passengers / cars_driven

# Prints out a string a value and then another string
# States the number of cars
print("There are", cars, "cars available.")
# States the number of drivers
print("There are only", drivers, "drivers available.")
# States number of cars not to be driven
print("There will be", cars_not_driven, "empty cars today.")
# States carpool capacity that is available
print("We can transport", carpool_capacity, "people today.")
# States the number of passengers to carpool
print("We have", passengers, "to carpool today.")
# states the average passenger count per car
print("We need to put about", average_passengers_per_car,
        "in each car.")

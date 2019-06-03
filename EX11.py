## Practice Typing code
## Learning Python 3 the Hardway
## Exercise 11

## Prints string and leaves a space for the response in input
print("How old are you?", end=' ')
## initiates age var with input as string
age = input()
## Prints question as a string with a space for the response
print("How tall are you?", end=' ')
## initiates height with input
height = input()
## asks used for there weight, leaves a space instead of newline
print("How much do you weigh?", end=' ')
## initiates weight with user input
weight = input()
## Combines age, height, and weight variables with string
print(f"So, you're {age} old, {height} tall and {weight} heavy.")


# Extras

print("What is your favorite color?", end=" ")
color = input()
print("What is your favorite book?", end=' ')
book = input()
print("What is your favorite movie?", end=' ')
movie = input()

print(f"Your favorites are the following: \nColor = {color}\nBook = {book} \nMovie = {movie}")

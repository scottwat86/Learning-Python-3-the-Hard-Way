## Practice Typing code
## Learning Python 3 the Hardway
## Exercise 10

## iniates string vars with tabs and new lines and \
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."


## Initiates the var with a multiline string
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

## prints the variable with strings
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Other Escape Sequences
# \\          backslash \
# \'          single quote
# \"          double quote
# \a          ASCII bell -> nothing is printed but rings a terminal bell
# \b          ASCII backspace
# \f          ASCII formfeed -> page-seciton seperator
# \n          next line
# \N{name}    Character named name in the unicode database
# \r          carriage Returns
# \t          tab
# \uxxxx      character with bit hex values
# Uxxxxxxxx   character with 32 bit ..
# \v          ASCII vertical tab
# \ooo        character with octal values
# \xhh        character with hex value hh

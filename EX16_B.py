# imports argv from sys module
from sys import argv
# Takes filename as target
script, target = argv
#Opens file reads to filecontent then auto closes
with open(target, "r") as file:
  file_content = file.read()
# prints file content
print(file_content)

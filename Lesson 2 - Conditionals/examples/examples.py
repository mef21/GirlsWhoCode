"""
WELCOME TO CONDITIONAL EXAMPLES

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd 'Lesson 2 - Conditionals'; clear; cd examples; python3 examples.py"


"""

""" EXAMPLE 1 """
if(1 < 2):
  print("1 is less than 2")
else:
  print("1 is not less than 2")

""" EXAMPLE 2 - with VARIABLES """
x = 5
y = 10
if(x < y):
  print("x is less than y")
else:
  print("x is not less than y")

""" EXAMPLE 3 - with EQUALS sign """
x = 5
y = 10
if(x == y):
  print("x is equal to y")
else:
  print("x is not equal to y")

""" EXAMPLE 4 - with ELIF """
x = 5
y = 5
if (x < y):
  print("x is less than y")
elif(x == y):
  print("x is equal to y")
else:
  print("x is greater than y")

""" EXAMPLE 5 - Nested if statements """
temperature = 80
if(temperature >= 80):
  print("It is hot")
  if(temperature >= 100):
    print("You should stay indoors")
  
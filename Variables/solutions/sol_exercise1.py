"""
WELCOME TO VARIABLES EXERCISE 1

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd Variables; cd solutions; python3 sol_exercise1.py"

For examples please refer to the example1.py file

Start with the base code below 

GOAL: Try to swap the variables color1 and color2

"""

""" BASE CODE STARTS HERE """

color1 = "red"
color2 = "blue"

""" YOUR CODE STARTS HERE """
temp_variable = color1
color1 = color2
color2 = temp_variable

""" CHECK YOUR RESULTS - DO NOT CHANGE CODE BELOW """
print("color1: " + color1)
print("color2: " + color2)

""" 
This should print out: 

color1: blue
color2: red

"""

""" EXPLAINATION 

In order for you to swap the variable values, you must use a temporary variable that stores the value of one of the variables. 

"""
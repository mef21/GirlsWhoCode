"""
WELCOME TO LISTS_IO_RANDOM SOLUTIONS EXERCISE 2

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd 'Lesson 3 - Lists, IO, Random'; cd solutions; clear; python3 sol_exercise2.py"

For examples please refer to the example files

Start with the base code below 

GOAL: Write to a file called "RandomNumbers.txt" the following text: 'Today’s lucky number is ' followed by a random number

"""

""" BASE CODE STARTS HERE - DO NOT CHANGE CODE BELOW """
import random

file_path = "../text_files/RandomNumbers.txt"

""" YOUR CODE STARTS HERE """

f = open(file_path, "w")
r = random.randrange(0,100,1)
contents =  'Today’s lucky number is ' + str(r)
f.write(contents)
f.close()

""" 
This should not print out anything but instead should create a file in the text_files directory. 
"""

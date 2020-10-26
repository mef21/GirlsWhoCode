"""
WELCOME TO FUNCTIONS EXERCISE 1 SOLUTION

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd 'Lesson 5 - Functions'; cd solutions; clear; python3 sol_exercise1.py"

For examples, please refer to the example files

Start with the base code below 

GOAL: 
Write two functions: count_down and count_up. 
count_down takes in two integers and counts down from the first integer to the second integer. Then it prints "Happy New Year!"

count_up takes in two integers and counts up from the first integer to the second integer. Then it prints "Take off!"

HINT: 
The skeleton to create a function is:
def function_name (parameters):
  Body of your function here

"""

""" YOUR CODE STARTS HERE """
def count_down(num1, num2):
  while num1 >= num2:
    print(num1)
    num1 -= 1
  print("Happy New Year!")

def count_up(num1, num2):
  while num1 <= num2:
    print(num1)
    num1 += 1
  print("Take off!")

""" BASE CODE STARTS HERE - DO NOT CHANGE CODE BELOW """
print("count down!")
count_down(10, 1)
print("count up!")
count_up(0, 10)



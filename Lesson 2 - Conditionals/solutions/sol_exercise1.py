"""
WELCOME TO CONDITIONALS SOLUTIONS EXERCISE 1

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd Conditionals; cd solutions; clear; python3 sol_exercise1.py"

For examples please refer to the example1.py file

Start with the base code below 

GOAL: Print out the variable yum or ok based on the users imput

"""

""" BASE CODE STARTS HERE - DO NOT CHANGE CODE BELOW """
yum = "YUMMM"
ok = "Ok! Come back another time!"

answer = input("Do you want to order a pizza? ")
reply = ""

""" YOUR CODE STARTS HERE """
if(answer == 'Yes' or answer == 'yes'):
  reply = yum
else:
  reply = ok

""" CHECK YOUR RESULTS - DO NOT CHANGE CODE BELOW """
print("answer: " + reply)

""" 
Your code should print out: 

if user answers "yes" or "Yes", display
  answer: YUMMM 
if the user replies with any other reply, display
  answer: "Ok! Come back another time!"

"""
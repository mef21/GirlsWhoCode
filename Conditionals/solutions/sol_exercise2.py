"""
WELCOME TO CONDITIONALS EXERCISE 2

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd Conditionals; cd 'Exercises and Examples'; cd solutions; python3 sol_exercise2.py"

For examples please refer to the example2.py file

Start with the base code below 

GOAL: Check to see if entered username and password are correct

"""

""" BASE CODE STARTS HERE - DO NOT CHANGE CODE BELOW """
username = "user1"
password = "password1"

useri = input("Enter username: ")
passi = input("Enter password: ")

""" YOUR CODE STARTS HERE """
if(useri == username):
  print("username correct")
  if(passi == password):
    print("password correct")


""" 
Your code should print out: 

if user enters proper username, display
  username correct
if user enters correct username and password, display
  password correct

"""
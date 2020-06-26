"""
WELCOME TO CONDITIONALS EXERCISE 3

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd Conditionals; cd 'Exercises and Examples'; cd solutions; python3 sol_exercise3.py"

For examples please refer to the example3.py file

Start with the base code below 

GOAL: Ask the user for their age. Determine if the user was born before or after 2000. Pretend it is 12/31 and everyone has already had their birthday this year

Challenge: determine if the user was born before 2000, after 2000 but before 2005, and after 2005 using if, elif, and else. 

"""

""" BASE CODE STARTS HERE - DO NOT CHANGE CODE BELOW """
age = int(input("How old are you? "))
# please note this will throw an error if the user does not provide a number

""" YOUR CODE STARTS HERE """
curr_year = 2020
year_born = curr_year - age
if(year_born < 2000):
  print("You were born before 2000.")
else:
  print("You were born during or after 2000.")

""" 
Your code should print out: 

If the user was born before 2000, print 
  You were born before 2000.
If the user was born during or after 2000, print 
  You were born during or after 2000.

"""
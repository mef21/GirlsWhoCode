"""
WELCOME TO LOOPS EXERCISE 2

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd 'Lesson 4 - Loops'; cd exercises; clear; python3 exercise2.py"

For examples, please refer to the example files

Start with the base code below 

GOAL: Create a menu that offers 3 options to the user and this menu will repeat until the user enters number 3, which will exit the program. If the user enters the number 1, they will be asked to enter 3 numbers, these numbers will be added together, and the user will be prompted by the menu_text again. If the user enters the number 2, they will be asked to enter 2 numbers, the numbers will be multiplied, and the user will be prompted by the menu_text again. If the user enters number 3, the program will print "Goodbye", exit, and the user will not be prompted again. 

If the user does not enter "1", "2", or "3", print "invalid choice" and reprint the menu 

Hint: Use a while loop to ask the prompt until the code exits

"""

""" BASE CODE STARTS HERE - DO NOT CHANGE CODE BELOW """

welcome_text = "Welcome to the Menu!"
menu_text = "Menu Choices: \n1 - addition\n2 - multiplication\n3 - exit\nPlease enter your choice: "
print(welcome_text)
user_input = "nothing yet"

""" YOUR CODE STARTS HERE """
 


""" This should print out:

When the user inputs numbers in the following order, 1,2,2,2,2,3,3,5,3 the below text should be printed out

Welcome to the Menu!
Menu Choices: 
1 - addition
2 - multiplication
3 - exit
Please enter your choice: 1
Enter the first number: 2
Enter the second number: 2
Enter the third number: 2
6
Menu Choices: 
1 - addition
2 - multiplication
3 - exit
Please enter your choice: 2
Enter the first number: 3
Enter the second number: 3
9
Menu Choices: 
1 - addition
2 - multiplication
3 - exit
Please enter your choice: 5
invalid choice
Menu Choices: 
1 - addition
2 - multiplication
3 - exit
Please enter your choice: 3
Goodbye

"""

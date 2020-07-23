"""
WELCOME TO FOR while EXAMPLES

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd 'Lesson 4 - Loops'; cd examples; clear; python3 while_examples.py"

"""
""" EXAMPLE 1
This loop continues to repeat until the inputted number by the user is equal to the value stored in the variable val. 
"""
is_val = "0"
val = "3" 
is_val = input("please enter a guess: ")
while(is_val != val): 
  print("\nthis while loop is executing again because the boolean is not true and the inputed number does not match the number saves in val")
  is_val = input("please enter a guess: ")

print("Finished executing the loop")


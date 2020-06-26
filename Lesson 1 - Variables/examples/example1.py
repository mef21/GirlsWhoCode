"""
WELCOME TO VARIABLES EXAMPLE 1

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd 'Lesson 1 - Variables'; cd examples; python3 example1.py"


Below are a series of examples using different types of variables and how to manipulate them: 

"""

""" STRING EXAMPLE

Print out the value of a_string with other text such that the output is - hello world! Have a great day! Python is cool.

"""
# Solution 1
a_string = "hello world"
print(a_string + "! Have a great day! Python is cool.")

# Solution 2
a_string = "hello world"
a_string = a_string + "! Have a great day! Python is cool."
print(a_string) 

# Solution 3
a_string = "hello world"
b_string = "! Have a great day! Python is cool."
print(a_string + b_string)

""" INTEGER/FLOAT EXAMPLE 

Add multiply and divide to print out - number: 10

""" 

# Solution 1 
num1 = 2
num2 = 10
num3 = (num1*num2)/2
print("number: " + str(num3))

# Solution 2 

num1 = 5
num2 = 4
num3 = 2
num4 = (num2/num3)*num1
print("number: " + str(num4))

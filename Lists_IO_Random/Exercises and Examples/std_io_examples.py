"""
WELCOME TO Standard Input and Output EXAMPLES

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd Lists_IO_Random; cd 'Exercises and Examples'; python3 std_io_examples.py"

"""
# Takes in a string
name = input("What is your name? ")
print(type(name))
print("Inputted Name: " + name)

# Takes in a number (int/float)
number = int(input("What is your favorite number? "))
print(type(number))
# need to recast to string to print back out
# casting - changing type of a variable
print("Inputted Number: " + str(number))
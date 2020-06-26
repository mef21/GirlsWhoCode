"""
WELCOME TO Random Number Generation EXAMPLES

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd Lists_IO_Random; cd 'Exercises and Examples'; python3 rand_examples.py"

"""

# LINE BELOW MUST ALWAYS BE INCLUDED
import random

# Will randomly choose one of these numbers
i1 = random.choice([0,1,2,3,4])
print("Random number generated: " + str(i1))
# Start at 0, end at 4, increment from 0 to 4 by 1 
i2 = random.randrange(0,4,1)
print("Random number generated: " + str(i2))
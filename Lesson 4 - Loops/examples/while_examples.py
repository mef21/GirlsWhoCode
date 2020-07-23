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

""" EXAMPLE 2
Sum up all of the numbers from 1 to 100
"""
sum1 = 0 
# this loop goes through all values of i from 1 to 100
i = 1
# also can use while i <= 100
while i < 101:
  # also can use sum1 = sum1 + i
  sum1 += i
  i += 1
print(sum1)

""" EXAMPLE 3
Print out all entires in an array on different lines
"""
arr = ['hello','my','name','is','mr.','duck']
i = 0 
while i < len(arr):
  print(arr[i])
  i += 1

""" EXAMPLE 4
Print out all entires in an array on the same line
"""

arr = ['hello','my','name','is','Mr.','duck']
total1 = ""
i = 0
while i < len(arr):
  # also can use total = total + arr[i]
  total1 += arr[i] + " "
  i += 1
print(total1)


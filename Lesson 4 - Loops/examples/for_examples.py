"""
WELCOME TO FOR LOOP EXAMPLES

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd 'Lesson 4 - Loops'; cd examples; python3 for_examples.py"

"""

""" EXAMPLE 1
Sum up all of the numbers from 1 to 100
"""
sum1 = 0 
# this loop goes through all values of i from 1 to 100
for i in range(1,101):
  # also can use sum1 = sum1 + i
  sum1 += i
print(sum1)

""" EXAMPLE 2
Print out all entires in an array on different lines
"""
# Method 1 
arr = ['hello','my','name','is','mr.','duck']
for i in range(0, len(arr)):
  print(arr[i])

# Method 2
for i in arr:
  print(i)

""" EXAMPLE 3
Print out all entires in an array on the same line
"""
# Method 1 
arr = ['hello','my','name','is','Mr.','duck']
total1 = ""
for i in range(0, len(arr)):
  # also can use total = total + arr[i]
  total1 += arr[i] + " "
print(total1)

# Method 2
total2 = ""
for i in arr:
  total2 += i + " "
print(total2)

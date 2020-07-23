"""
WELCOME TO FUNCTION EXAMPLES 2

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd 'Lesson 5 - Functions'; cd examples; clear; python3 example2.py"

"""


def add_two(arr): 
  for i in range(0, (len(arr))):
    arr[i]= arr[i] + 2
  return arr

def count_as(arr):
  count = 0 
  for i in arr:
    if (i == 'a'): 
      count +=1
  return count 

def add_twoo(arr): 
  for i in range(0, len(arr)): 
    if(arr[i] > 10):
      arr[i] += 2
  return arr

print(add_twoo([6, 8, 9, 10, 11, 15, 12, 50]))
print(add_two([6, 8, 9, 10, 11, 15, 12, 50]))

print(add_two([1,2,4,5]))
print(count_as(['w', 'a', 'r', 'a', 'a']))
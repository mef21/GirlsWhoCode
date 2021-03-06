"""
WELCOME TO LOOPS SOLUTIONS EXERCISE 1

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd 'Lesson 4 - Loops'; cd solutions; clear; python3 sol_exercise1.py"

For examples, please refer to the example files

Start with the base code below 

GOAL: for each word in an array, print out "vowel" if the first letter of the word is a vowel or print out "consonant" if the first letter of the word is a consonant. 

Hint1: Use an if statement inside of the loop
Hint2: google "extract first letter from string in python"
"""

""" BASE CODE STARTS HERE - DO NOT CHANGE CODE BELOW """
words = ["keyboard", "mouse", "apple", "computer", "orange", "headphones", "if", "else", "trackpad", "monitor", "terminal", "taskbar", "foo", "bar"]
vowels = ["a","e","i","o","u"]

""" YOUR CODE STARTS HERE """
# Method 1
for e in words:
  if(e[:1] in vowels):
    print("vowel")
  else:
    print("consonant")

# Method 2
for e in range(0, len(words)):
  if(words[e][0] in vowels):
    print("vowel")
  else:
    print("consonant")


""" This should print out:
consonant
consonant
vowel
consonant
vowel
consonant
vowel
vowel
consonant
consonant
consonant
consonant
consonant
consonant
"""

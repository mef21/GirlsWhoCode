# Conditionals
## Definition:
A statement that tells a program to perform different actions depending on whether a condition is true or false
## Real Life Examples:
* __IF__ I had a talking penguin, I would be so happy
* __IF__ you pay attention to this class, you will learn what to do with a talking penguin. __ELSE__, you might miss something.
## In Python: if and else
```python
if( condition ):
  # This code will run if condition is true
else:
  # This code will run if condition is false
```
### How to:
* if and else need to be lowercase
* Parentheses () are *optional* around the condition
* Colon : is __required__ after the condition and after the else
* Code inside the if and else blocks need to be indented (press tab)
#### Example:
```python
if(1 < 2):
  print("1 is less than 2")
else:
  print("1 is not less than 2")
```
#### Example With Variables:
```python
x = 5
y = 10
if(x < y):
  print("x is less than y")
else:
  print("x is not less than y")
```
### Checking for Equality
* We use one equals sign to assign a value to a variable
```python
x = 5
```
* To check for equality, we use __TWO__ equal signs
```python
if(x == y):
```
#### Example:
* Note the use of __TWO__ equal signs below
```python
x = 5
y = 10
if(x == y):
  print("x is equal to y")
else:
  print("x is not equal to y")
```
#### Example without *else* statement
* We can have an if statement without an else statement
* When the condition in the if statement is false, nothing will happen
```python
x = 5
y = 10
if(x == y):
  print("x is equal to y")
```
## In Python: elif
* We just learned __if__ and __else__
* There is another keyword called __elif__
* __elif__ is used when we want to have if statements that get checked after the first if
* __elif__ gets used between if an else and is used when you want additional checks after the condition in the first if statement fails
### Real Life Example:
* __if__ you choose a burger for lunch, you pay $5
* __elif__ you choose chicken nuggets for lunch, you pay $7
* __else__, you don't deat anything for lunch and you don't pay
In the above example you only get 1 of the 3 options. You cannot get both a burger and chicken nuggets
### Python Example:
```python
x = 5
y = 5
if (x < y):
  print("x is less than y")
elif(x == y):
  print("x is equal to y")
else:
  print("x is greater than y")
```
* You can have as many elif's as you want
* Combos:
  * if
  * if, else
  * if, elif
  * if, elif, else
  * if, elif, elif, elif, elif, else
  * ...
## Conditional Statement's Summary:
```python
if( condition ):
  # if the condition is correct, then this code will execute
elif ( condition2 ):
  # if condition is incorrect, and condition2 is correct, then this code will execute
else:
  # if neither condtions are correct, then this code will execute
```
## Boolean Operators
### Definition
Boolean operators are symbols or words to represent English logic and make comparisons
### Examples
* 5 is __equal__ to 5
* 4 is __less than__ 6
* 10 is __less than or equal to__ 10
### In Python: Operators

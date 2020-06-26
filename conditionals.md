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
#### Equality 
* ==
* Examples:
  * if(10 == 10)
  * if(5 == 10)
  * if(string == "hello world") 
#### Less Than, Greater Than
* <, >
* Examples:
  * if (4 < 5)
  * if (5 > 5)
#### Less Than or Equal, Greater Than or Equal
* <=, >=
* Examples
  * if(4 <= 5)
  * if(5 >= 5)
#### Operators and Parentheses
* We use parentheses to make conditionals more readable adn the logic more clear
* Do things inside parentheses first
  * Like PEMDAS in math!
* Examples:
  * if( 4 + 9 + 9 == 9 * 2)
  * if( (4 + 9 + 9) == (9 * 2))
### In Python: User Input
#### How To:
* Oftentimes you are going to want to ask the user for input and make decisions based on this input
* Example:
```python
answer = input("Are you happy? ")
if(answer == "Yes"):
  print("I'm glad you are happy! :)")
else:
  print("Don't be sad. Be GLAD")
```
### In Python: Nesting
* You can put if/elif/else statements inside other if/elif/else statements
* Example:
```python
temperature = 80
if(temperature >= 80):
  print("It is hot")
  if(temperature >= 100):
    print("You should stay indoors")
```
### In Python: Boolean Operators
*Examples of Boolean Operators
  * If you pay attention to this class __and__ you ask questions, you will learn Python. Else, you might miss something.
  * If you know python __or__ javascript, you can code.
#### Operator: __and__
* All conditions have to be true for the statement to be true
* Examples:
  * if(10 == 10 __and__ 5 == 5)
  * if(string == "hello" and 1 == 1)
#### Operator: __or__
* Only one condition has to be true for the statement to be true
* Examples:
  * if (1 == 10 __or__ 5 == 5)
  * if (5 == 10 __or__ 1 == 1)
####  Operator: __not__
* !
* Examples:
  * if(4 != 5)
  * if(5 != 5)
  * Tricky because you have to remember to flip
    * True --> False
    * False --> True

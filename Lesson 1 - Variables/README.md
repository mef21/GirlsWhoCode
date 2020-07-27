# Variables
Definition: Something that stores other things
## What is a Variable? 

Variables are used to store information to be referenced and manipulated in a computer program. They also provide a way of labeling data with a descriptive name, so our programs can be understood more clearly by the reader and ourselves. It is helpful to think of variables as containers that hold information. Their sole purpose is to label and store data in memory. This data can then be used throughout your program.

Here are three example sentences: 

* I like ice cream and french fries
* You like ice cream and french fries
* My neighbor likes ice cream and french fries

To change “ice cream and french fries” you have to change it in three different places (too much work)! We can use a variable X instead to represent the repeated values. 

X = ice cream and french fries

I like X
You like X
My neighbor likes X

When you read the sentence across, you can replace the X with the value stored in X. 

In order to store something in a variable in any computer programing language you will always have the name of the variable on the lefthand side and the value you want to store in the variable on the right hand side. 
```python
variables_are_cool = 10
```
## In Python
Variable Names:
You can name any your variables whatever you like but you need to follow some rules that are listed below. 
* Separate words by _ (NOT SPACES)
* Make the variable name descriptive
* try not to make them too long because you will need to type them many time
* Cannot start with number or symbol (!, @, etc.)

### Python Variable Types:

* Strings: collection of letters, numbers or symbols in double quotes
  * Think of strings are words contained in double quotes
  * Ex: "Hello, my name is Maddy"
* Chars: single letter, number, or symbol in single quotes
  * Similar to strings but only one letter
  * Ex: 'a', ';', ' ', '!', etc.
* Integer: Whole numbers
  * Ex: 1, 5, 463836, -472, 36283
* Floats: decimal numbers
  * Ex: 0.0, -1.0, 1.5, 3.1483
* Boolean: True or False expression
  * Ex: True, False, (7 > 0)

#### Strings:
Strings need quotes around words:
variable_name = "words, letters, or numbers"
Ex:
```python
favorite_food = "ice cream and french fries"
```
#### Numbers:
variable_name = number value
Ex:
```python
five_as_an_integer = 5
five_as_a_float = 5.0
```
#### Booleans:
variable_name = True or False
Ex:
```python
likes_ice_cream = True
```
### In Python: Let's Do Some Math!
#### Operations:
* Addition (5 \+ 5)
* Subtraction (10 \- 3)
* Multiplication ( 3 \* 1)
* Division (6 \/ 2)
#### Order of Operations
* Parentheses
* Exponent
* Multiplication
* Division
* Addition
* Subtraction
#### Modulus: %
[![Modulus Video](http://img.youtube.com/vi/MrTtsX2Wg9Q/0.jpg)](http://www.youtube.com/watch?v=MrTtsX2Wg9Q "Modulus Operator - CS101 - Udacity")

Remainder
* Leftover from division
* Ex:
  * 6 % 3 = 0
  * 2 % 3 = 2
  * 10 % 3 = 1
* Anything % 10 results in the last digit
* Ex:
  * 123 % 10 = 3
  * 12 % 10 = 2
  * 1 % 10 = 1

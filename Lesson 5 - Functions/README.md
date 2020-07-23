# Functions
## Definition
A function is a block of code that only runs when it is called. You can pass data into functions, as well as return data as a result of the function being called. 
## Parts of a Function
The following code snippet is an example of what a function looks like in python:
```python
def printSum( num1, num1 ):
  sum = num1 + num2
  return(sum)
```
1. __def__ - This keyword tells the computer you're creating a function
2. __printSum__ - This is the name of the function
3. __num1,num2__ - These are the __parameters__, or information that the function needs. Notice they are always between "()"
4. __:__ - This indicates where the function begins. All indented text is inside of the function
5. Function Body - The function body is the lines of code that are indented after the __:__ that make your function work. See below:
  * ```python
    sum = num1 + num2
    return(sum)
    ```
6. __return(sum)__ - "return" is used in order to specify what the function should return. The value inside the "()" is what is returned by the function 

The following image is a visual representation of the function above:
<br>
<p align="center"><img src="https://github.com/mef21/GirlsWhoCode/blob/master/Images/Function.png" width="400" height="275"></img></p>

The parameters go into the function __(num1,num2)__, the function uses the parameters in the __Function Body__, and then the sum is returned from the function.

### Why Does This Matter?
The following two code snippets do the exact same thing:
#### 1
```python
 # Start of File
 def printSum(num1,num2):
   sum = num1 + num2
   return(sum)
 print(printSum(1,4))
```
#### 2
```python
# Start of File
sum = 1+4
print(sum)  
``` 
However, the first code snippet is more versatile because it can be reused with different variable values, and does not require as much manual modification to your code. When you have to do the same action many times, it will let you repeat the action with one line instead of writing the body of the function many times.

## Returning Functions vs Non-Returning Functions
Not all functions need to return a value. A great example of a function that does not return a value is the following:
```python
def special_print(number):
  for i in range(number):
      print('''
             /^\/^\\
           _|__|  O|
  \/     /~     \_/ \\
   \____|__________/  \\
          \_______      \\
                  `\     \                 \\
                    |     |                  \\
                   /      /                    \\
                  /     /                       \\\\
                /      /                         \ \\
               /     /                            \  \\
             /     /             _----_            \   \\
            /     /           _-~      ~-_         |   |
           (      (        _-~    _--_    ~-_     _/   |
            \      ~-____-~    _-~    ~-_    ~-_-~    /
              ~-_           _-~          ~-_       _-~
                 ~--______-~                ~-___-~
      ''')
```
The function above is used to print out the ASCII snake, and the number of times it is printed is specified by the number parameter. This is just one example of a function that does not return a value, but there are many other examples as well.

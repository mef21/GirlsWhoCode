# Lists, IO, and Random Numbers
## Lists
### Definition
A list is used to store __multiple values__ of the __same type__ in __one single variable__
### In Python: Lists
* Syntax:
  * list_name = [1, 2, 3, 4, 5, 6]
* Example:
```python
best_movies = ["Big Hero 6", "Avengers", "Quiet Place"]

weekends = ["Saturday", "Sunday"]

ages = [15, 16, 20, 18]
```
* Notice in the examples above, all of the lists containt multiple elements of the __same type__
#### List Indexing
* Index: where an element is in a list
* List indices start at 0 and end at (length of array -1)
* Example:
    | 0 | 1 | 2 | 3 |
    | ----- | ----- | ----- | ----- |
    | "Big Hero 6" | "Avengers" | "Quiet Place" | "Martian" |
* The length of this array is 4
 * In order to reference the last movie in this array, we need to reference it by its index which can be found in the following way:
  ```python
  len(best_movies) - 1
  ```
* "Quiet Place" is at index 2
* At index 0, the movies is "Big Hero 6"
* We can set the movie at the 0 index using the following code snippet:
```python
best_movies[0] = "Spiderman"
```
* The result will now be:
    | 0 | 1 | 2 | 3 |
    | ----- | ----- | ----- | ----- |
    | "Spiderman" | "Avengers" | "Quiet Place" | "Martian" |
    
### Review
[![Python List Video](http://img.youtube.com/vi/ohCDWZgNIU0/0.jpg)](http://www.youtube.com/watch?v=ohCDWZgNIU0 "Python Lists || Python Tutorial || Learn Python Programming")
## IO
### User Input
```python
name = input("What is your name? ")
```
* In the snippet above, the user input is stored in the variable called "name"
```python
number = int(input("What is your favorite number? "))
```
* In the code snippet you are storing the user input in the variable called "number"
* We are casting the input to an int because we want the variable to be of type int
 * By default, the type is string. This is why we cast it to an int
### File I/O
* Python provides basic functions and methods necessary to manipulate files by default
* Python uses the built-in file object
#### File Modes
* Use the "r" mode to open reading
* Example:
```python
f = open("hello.txt", "r") # open for reading in text mode
contents = f.read() # store the whole file into memory
```
* Use the "w" mode to open for writing
* Example:
```python
f = open("hello.txt", "w") # open for writing, create if necessary
f.write("Hello, file!\n") # write string to file; notice \n ending
```
## Random Numbers
### Import Random Library
* At the top of your code, add the following line:
```python
import random
```
### Random Functions:
* The following code will randomly choose one of the numbers in the array, and store it in the variable x
```python
x = random.choice([0, 1, 2, 3, 4])
```
* The following code will create an array starting at 0, ending at 4, and will include all numbers in between the start and the end incrementing from the start by the incrementer which is 1.
* In the following code, the array will be created, and then one of the numbers from that array, will be selected and stored in the variable x
```python
x = random.randrange(0,4,1)
```
#### Random Range
* Choice () --> generate a random number from a container
* Example:
```python
random.choice([1, 4, 8, 10, 3])
```
 * Example Answer: 4
* randrange(beg, end, step) --> generate a random number but within a range specified by the arguments
  * beg = beginning number
  * end = last number
  * step = to skip numbers in range while selecting
 ```python
 random.randrange(20, 50, 3)
 ```
 * Example Answer: 41

# Turtle
## Definition
Tutle is a pre-installed Python library that allows you to create pictures and shapes by providing a virtual canvas. The onscreen pen that is used for drawing is called the __turtle__
## Using Turtle
```python
import turtle
ted = turtle.Turtle()
ted.shape("turtle")

# This is where your code goes

turtle.done()
```
### Basic Movement
* Moving forward
```python
ted.forward(100) # move forward 100 pixels
```
* Rotating Left and right
```python
ted.left(30) # rotate left 30 degrees
ted.right(30) # rotate right 30 degrees
```
### Using Functions with Turtle
As was discussed in Lesson 5 - Functions, functions are a great way to repeat the same actions more than once, without duplicate code being written. Lets use a function in order to draw a triangle with turtle. We are going to break down this function creation into a series of steps:

#### Step 1
We first need to understand the basic geometry of the triangle. We know that it has three sides, but what about the angle between each side? In order to figure out how many degrees the turtle should turn in order to get the correct angle, we can divide 360 by the number of sides of the shape. That being said, __360 / 3 (sides of a triangle) = 120__. So now we know that we need the turtle to turn __120 degrees__ in order for the angles to be correct.
#### Step 2
Now that we know a triangle needs 3 sides, and after each side we have to turn 120 degrees, we also need to consider the length of the sides. We are going to utilize parameters into our function, in order to do this for us. By having the side length as a parameter, we are able to draw multiple different triangles, that are all different sizes.
#### Step 3
Now that we have a pretty good idea of how our function is going to look, we can start to create it. It should look like the following based on what information we know so far:
```python
def draw_trianlge(side_length):
  # Function Body
```
#### Step 4
Drawing a triangle can be summarized in the following steps:
* Move forward the length of the side
* Turn left 120 degrees
* __repeat 2 more times__
  * We can utilize what we learned in Lesson 4 - Loops to make our code more efficient

#### Step 5
Now we can put it all together and write the Function body for the draw_triangle function:
```python
def draw_trianlge(side_length):
  for i in range(3): # The number is 3 because a triangle has 3 sides
    ted.forward(side_length)
    ted.left(120)
```

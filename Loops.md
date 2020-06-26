# Loops
## Definition
Loops are a way for programmers to quickly __repeat__ a task until a __condition__ has been met
### While Loops
There are 4 parts to a while loop
1. __while__
    * key word for the computer to know you are starting a while loop
2. __(boolean)__
    * this is what you are checking to see if it is true or false
3. __:__
    * follows the parentheses and tells the computer you are finished checking your boolean
4. __(body)__
    * on the line following the ":". Must be indented. This is the step you want to repeat multiple times
* Example:
```python
count = 2
sum2 = 0

while(count != 8):
  sum2 += count
  count += 1

print(sum2)
```
* *Must increment the count variable in order to avoid infinite loops*
* The output of the code snippet above will be __28__
  * The while loop is essentially doing a summation of numbers 0-7
### For Loops
There are 4 parts to a for loop
1. __for__
   * key word for the computer to know you are starting a for loop
2. __(variable)__
   * used to reference current spot in for loop
3. __in__
4. __(range)__
   * creates a list of whole numbers starting from the first number and ending at the (last number - 1)
5. __:__
   * follows the parentheses and tells the computer you are finished checking your boolean
#### Range
* What is range()?
* Examples:
    | range()  | values          |
    | -------- | --------------- |
    | range(4) | [0, 1, 2, 3, 4] |
    | range(1, 5) | [1, 2, 3, 4] |
### Uses for a "for loop"
* A for loop can be used to make printing every element in a list easier
* Example:
```python
shopping_list = ["bread", "jam", "marmite"]
for item in shopping_list:
  print(item)
```
* The output for the snippet above is:
  * bread
  * jam
  * marmite
* A for loop can also be used in order to count over numbers in a given range
* Example:
```python
print(range(-10, 1))
```
* The output of the above snippet is: [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0]

"""
WELCOME TO VARIABLES EXAMPLE 2

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd Variables; cd 'Exercises and Examples'; python3 example2.py"


Below are a series of examples using different types of variables and how to manipulate them: 

"""

""" BOOLEAN EXAMPLE

print out True in 8 different ways
print out False in 5 different ways

"""
var1 = True
print(var1)
var2 = (4 < 5)
print(var2)
var3 = (2 == 2)
print(var3)
var4 = (-1 != 6)
print(var4)
var5 = (7 >= 7)
print(var5)
var6 = (var4 or False)
print(var6)
var7 = (var5 or var2)
print(var7)
var8 = (var1 and var2)
print(var8)

var1 = False
print(var1)
var2 = (4 >= 5)
print(var2)
var3 = (2 != 2)
print(var3)
var4 = (-1 == 6)
print(var4)
var5 = (7 > 7)
print(var5)
var6 = (var4 or False)
print(var6)
var7 = (var5 or var2)
print(var7)
var8 = (var1 and not var2)
print(var8)
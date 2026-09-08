# Python syntax or Indentation
# Indentation mens spaces at the beginning of a code line 
# ex
''' 
if 5 > 2:
print("5 is grater than 2") this is an indentation

'''
#######################################################################

# Variables
"Varibale are containers for storing data Values"

# How to Create the Variable
''' 
x = 5
y = 2
print(x)
print(y)

'''

# Type Casting 
"if you want to specify the data type of a variable,this can be done with casting."
'''
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

'''

# Get The Type
"you can get the data type of varibale with the type(). function"
''' 
x = 5
y = "swop"
print(type(x))
print(type(y))

'''

#  String Varibale can be declared either by using single or double quotes:
'''
x = "John"
# is the same as
x = 'John'

'''

# Case-Sensitive
"Varible names are case-sensitive."
'''
a = 4
A = "Swop"
# A will not overwrite a
print(A)
print(a) 
'''

# variables
'''
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)

'''

# Multi Words Variable Names
'''
# 1. Camel-Case
Each word, except the first, starts with a capital letter:
 ex:-  myVariableName = "Swop"

# 2. Pascal-Case
Each word starts with a capital letter:
 ex:-  MyVariableName = "John"

# 3.Snake-Case
Each word is separated by an underscore character:
 ex:-  my_variable_name = "John"

'''

# Many Values to Multiple Variables
'''
x,y,z = "orange","banana","cherry"
print(x,y,z)
# print(x)
# print(x)
'''

# One Value to Multiple Variables
'''x = y = z = "Orange"
print(x,y,z)
'''

# Unpack Collection 
'''if you have a collection of values in a list,tuple etc. python allow,
you to extract the values into variable this is called unpacking.

fruits = ["apple","banana","cherry"]
print(fruits)
# x,y,z = fruits
# print(x,y,z)
'''

# Global Variables
'''
Global variables can be used by everyone, both inside of functions and outside.

x = "swop"
def fun():
    print("python is " + x)
fun()
'''

'''
x = "awesome"

def myfunc():
#   global x    if we remove this the o/p shoulbe be Python is awesome and if we add this then the o/p is Python is fantastic 
  x = "fantastic"

myfunc()

print("Python is " + x)
'''

# String
"Sting in python are surrounded by either single quotation mark, or double quotation mark"
#  Check string
'''
"To check if a certain phrase or character is present in a string, we can use the keyword in."
txt = "The best things in life are free !"
print("free" in txt)
'''


# List
'''
list are used to store multiple item in a single variable.
list are one of 4 built-in data types in python used to store collection of data
and list items are orderd,changeable and allow duplicate value

Ordered :- when we say that lists are ordered,it means that the items have defined order,
and that order will not change if you add new items to a list,the new items will be 
placed at the end of the list.

ex:- 

mylist = ["apple","banana","cherry"]
print(type(mylist))

'''
'''
mylist = ["apple","banana","cherry"]
print(mylist)
# identify type 
print(type(mylist))
# Access items
print(mylist[0])
# Negative indexing
print(mylist[-1])
# Range of index
print(mylist[0:2])
'''
'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# thislist.insert(2,"watermelon")
# thislist.append("orange")
# thislist.remove("mango")
thislist.pop(1) # this is also help to remove element
print(thislist)
'''

# Loop Through a list
# mylist = ["apple","banana","cherry"]
# # for x in mylist:
# #     print(x)
# for i in range(len(mylist)):
#     print(mylist[i])

# Using a While Loop
# mylist = ["apple","banana","cherry"]
# i = 0
# while i < len(mylist):
#     print(mylist[i])
#     i = i +1


# List Comprehension
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# Defination :- List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# The Syntax:- newlist = [expression for item in iterable if condition == True]



# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)


# Copy List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
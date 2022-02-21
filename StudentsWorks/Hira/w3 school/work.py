print("hlw my name hira ")

num1 = 2
num2 = 3
print(num1 + num2)

x, y = (3, 4)
print(x)

# Python - Slicing Strings
b = "hlw my name Ahira"
print(b[:2])
print(b[2:])
print(b[2:8])
print(b[6:9])
print(b[7:9])
print(b[7:10])
# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
print(b[-5:-2])
# Modify Strings

print(b.upper())
text = "I COULD NOT LIT IT GO FOR MORE THEN 20k TK"

'''
14/2/2020
https://www.w3schools.com/python/python_syntax.asp
"Python Indentation"
Indentation refers to the spaces at the beginning of a code line.
Where in other programming languages the indentation in code is for readability only,
the indentation in Python is very important.
Python uses indentation to indicate a block of code.
'''
# right way
if 5 > 2:
    print("Five is greater than two!")  # if e pore space tai holo ai khane indentation
# wrong way
'''
if 3==2:
print("3 equal 2 is not true ")
Python will give you an error if you skip the indentation:
'''

# right way
if 2 == 2:
    print("2 is equal 2 ")
if 3 < 5:
    print("3 is less than 5!")

# right way
if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!")

# wrong way
'''
if 5 > 2:
 print("Five is greater than two!")
      print("Five is greater than two!")
'''
if 5 > 2:
    print("Five is greater than two! ")
    print("and this is a right way")


'''
https://www.w3schools.com/python/python_variables_multiple.asp
Date : 15/2/2020a~!

Python Variables - Assign Multiple Values
Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:


'''
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#One Value to Multiple Variables

x = y = z = "apply"
print(x)
print(y)
print(z)

'''
Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
'''

fruits = ['banana', 'apple', 'orange']
x ,y ,z = fruits
print(x)


'''
Python - Global Variables
Date : 16/2/2022

Variables that are created outside of a function.Global variables can be used by everyone, both inside of functions and outside.
Create a variable outside of a function, and use it inside the function

'''

a = "awesome"

def myfunc():
  print("Python is " + a)

myfunc()

text = "python"

def myText():
    print('i love', text)

myText()
'''
Create a variable inside a function, with the same name as the global variable
'''

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#To create a global variable inside a function, you can use the global keyword.
#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "yoo"

myfunc()

print("Python is " + x)
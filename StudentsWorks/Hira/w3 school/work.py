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

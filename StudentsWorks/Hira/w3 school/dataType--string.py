'''
https://www.w3schools.com/python/python_datatypes.asp
Date : 19 / 2 / 2022

---------------------------------- Python Data Types -----------------------------------

Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview


Getting the Data Type
You can get the data type of any object by using the type() function:
'''

x = "Hira"
print(type(x))

x1 = ["apple", "banana", "cherry"]
print("This x1 is list data type ", type(x1))

x2 = ("apple", "banana", "cherry")
print("This x2 is tuple data type", type(x2))

x3 = ("apple", "banana", "cherry", 3, 6, 3, 1, 6)
print("This x3 is tuple data type", type(x3))

# x4 =("apple", "banana", "cherry",[name : "hira"])  #wrong

x5 = {"apple", "banana", "cherry"}
print("This x5 is set data ype", type(x5))

x6 = {"name": "John", "age": 36}
print("This is dict data type", type(x6))

x7 = frozenset({"apple", "banana", "cherry"})
print("This x7 is frozenset data type", type(x7))

x8 = b"Hello python"
print("This x8 is bytes data type", type(x8))
# len
print(len(x8))
x9 = bytearray(5)
print("This x9 is bytearray data type ", type(x9))

x10 = frozenset(("apple", "banana", "cherry"))
# display
print(x10)
print(type(x10))

x11 = memoryview(bytes(5))
# display
print("wow ! now see the mamory view ", x11)
print("This x11 is memoryview data type", type(x11))

x12 = range(10)
print(x12)
print(type(x12))

''' when i use this data type  in my code  . need to write the Setting the Specific Data Type
If  i  want to specify the data type  ' যখন আমি আমার কোডে এই ডেটা টাইপ ব্যবহার করি। নির্দিষ্ট ডেটা টাইপ সেটিং লিখতে হবে
যদি আমি ডেটা টাইপ নির্দিষ্ট করতে চাই'''

# Example	Data Type
x = str("Hello World")
x1 = int(20)
x2 = float(20.5)
x3 = complex(1j)
x4 = list(("apple", "banana", "cherry"))
x5 = tuple(("apple", "banana", "cherry"))
x6 = range(6)
x7 = dict(name="John", age=36)
x8 = set(("apple", "chips", "cherry"))
x9 = frozenset(("apple", "banana", "cherry"))



'''
https://www.w3schools.com/python/python_numbers.asp
Date  : 20/ 2 /2022

'''

'''
------------------------------------ Random Number --------------------------------------

Python does  "not" have a random() function to make a random number, 
but Python has a "built-in module" called random that can be used to make random numbers:

Import the random module, and display a random number between 1 and 9:
'''
import random
print("Here is show a random number between 1 to 10 : ", random.randrange(1, 10))


'''
https://www.w3schools.com/python/python_casting.asp
 #python casting -  There may be times when you want to specify a type on to a variable.
 This can be done with casting.
 its works for Specify a Variable Type
 int()
 float()
 srt()
 
'''

"""
------------------------------- Python Strings --------------------------------------

"""
myName = 'hira'
print(myName)
'''
(((Multiline Strings)))
You can assign a multiline string to a variable by using ''''''three'''''' quotes:
'''
text = ''' 
I am Hira ,
I love coffee,
I love my family ,
I have a pet cat '''
print(text)


'''
(((Strings are Arrays)))
Like many other popular programming languages, 
strings in Python are arrays of bytes representing unicode characters.

However, """"Python does not have a character data type"""", a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

every element can be a cut and it can be show the user 
'''
a = "Hello, World!"
print(a[0])
print(a[1])
print(a[0])
print(a[1])
print(a[0])
print(a[1])
print("\n")
'''
(((Looping Through a String)) একটি স্ট্রিং মাধ্যমে লুপ
Since strings are arrays, we can loop through the characters in a string, with a for loop.

যেহেতু স্ট্রিংগুলি array , আমরা একটি স্ট্রিংয়ের অক্ষরগুলির মধ্যে লুপ করতে পারি, একটি ফর লুপ দিয়ে।
'''
print("Looping Through a String")
for x in 'myname':
    print(x)



'''
22 / 2 / 2022
(((Check String)))
To check if a certain phrase or character is present in a string, we can use the keyword in.

Example
Check if "java" is present in the following text:

'''


txt = "i love python" # String
print("java" in txt)
# output : false
name_of_people =["hira", "dany", "hafiz"]  # list
print("hira" in name_of_people)
# output: true
# output dey true and false value show kore na

# another way
# Use it in an if statement:
mytext = "People get what they do"
if "they" in mytext:
    print("yes i found ")  # true false theke ber hoyte parlam

"""
((( Check if NOT )))
To check if a certain phrase or character is NOT present in a string, we can use the keyword "not in"
"""

txt = "The best things in life are free!"
print("expensive" not in txt)
print("are" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("yes ! expensive is not found ")


'''
23 /2 /2022
((( Python - Slicing Strings )))
ou can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

Example
Get the characters from position 2 to position 5 (not included):
'''

b = "Hello, World!"
print("the characters from position 2 to position 5",b[2:5])

# (((Slice From the Start)))
name = "water"
print(name[:2])

# (((Slice From the End)))
name = "apple"
print(name[2:])

b = "Hello, World!"
print(b[-5:-2])

'''
Python - Modify Strings

'''
#upper case
a = "hlw"
b =  "python"
text = a.upper()
print(text)
print(b.upper())

a = "Hello, World!"
print(a.lower())

'''
(((Remove Whitespace)))
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

Example
The strip() method removes any whitespace from the beginning or the end:


'''

a = "                    Hello, World! "
print(a)
print(a.strip())
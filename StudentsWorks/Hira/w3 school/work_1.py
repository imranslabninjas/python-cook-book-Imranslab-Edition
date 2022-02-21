'''
https://www.w3schools.com/python/python_datatypes.asp
Date : 19 / 2 / 2022

Python Data Types

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
Random Number
Python does  "not" have a random() function to make a random number, 
but Python has a "built-in module" called random that can be used to make random numbers:

Import the random module, and display a random number between 1 and 9:
'''
import random
print("Here is show a random number between 1 to 10 : ", random.randrange(1, 10))


'''
https://www.w3schools.com/python/python_casting.asp
 python casting -  There may be times when you want to specify a type on to a variable.
 This can be done with casting.
 its works for Specify a Variable Type
 int()
 float()
 srt()
 
'''

"""
Python Strings

"""
myName = 'hira'
print(myName)
'''
Multiline Strings
You can assign a multiline string to a variable by using ''''''three'''''' quotes:
'''
text = ''' 
I am Hira ,
I love coffee,
I love my family ,
I have a pet cat '''
print(text)


'''
Strings are Arrays
Like many other popular programming languages, 
strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

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

print("Looping Through a String")
for x in 'myname':
    print(x)



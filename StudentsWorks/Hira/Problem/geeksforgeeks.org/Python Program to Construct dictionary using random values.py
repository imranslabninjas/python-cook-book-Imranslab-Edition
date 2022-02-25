'''
Date: 25/2/2022
Python Program to Construct dictionary using random values.
এলোমেলো মান ব্যবহার করে অভিধান তৈরি করতে পাইথন program
-- Given List, our task is to write a Python program
to construct dictionary with values randomly selected from range.--

Examples:

Input : test_list = ["Gfg", "is", "Best"], i, j = 2, 9
Output : {'Gfg': 3, 'is': 9, 'Best': 4}
Explanation : Random values assigned between 2 and 9.

Input : test_list = ["Gfg", "is", "Best"], i, j = 2, 10
Output : {'Gfg': 3, 'is': 9, 'Best': 10}
Explanation : Random values assigned between 2 and 10.


Method #1 : Using randint() + loop

In this, we iterate through each element in list and assign random number selected
using randint() to construct key value pair dictionary.
'''
# Using randint() + loop
from random import randint

# initializing list
test_list = ["Gfg", "is", "Best"]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
i, j = 2, 9

res = dict()
for ele in test_list:
    # assigning random elements
    res[ele] = randint(i, j)

# printing result
print("Random range initialized dictionary : " + str(res))

''' 
what is randint in python ? 
ANSWER- The randint() method returns an integer number selected element from the specified range. 
Note: This method is an alias for randrange(start, stop+1) .
https://www.w3schools.com/python/ref_random_randint.asp#:~:text=The%20randint()%20method%20returns,start%2C%20stop%2B1)%20.
1st:
import random

print(random.randint(3, 9))


what is dict() function? 
ANSWER: The dict() function creates a dictionary.
A dictionary is a collection which is unordered, changeable and indexed.

2nd:
x = dict(name = "John", age = 36, country = "Norway")

print(x)
print(type(x))

x = dict{name = "John", age = 36, country = "Norway"}
x = dict[name = "John", age = 36, country = "Norway"]
ai vabe kaj kore na .() only 


'''

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Put all keys of `dict1` in a list and returns the list
print(dict1.keys())
print(dict1.values())

a = {'apple': 'fruit', 'beetroot': 'vegetable', 'cake': 'dessert'}
print(a['apple'])



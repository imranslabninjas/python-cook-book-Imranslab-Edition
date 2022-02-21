"""
9 :  Write a Python function which takes a dictionary as an input argument and returns a boolean value, the boolean value
represents if the dictionary is Empty or has some element in it. It should be able to take an empty dictionary or a dictionary
with keys no more than 20 elements. A simple structure is given to make your understanding better.
Def isDictionaryEmpty(dictionary):
Return isDictEmpty  #How do you understand this is empty
"""

dict = {}
def empty_dict(dictionary):
    """ This empty_dict() method will retun boolean value True if empty otherwise False"""
    return not bool(dictionary)

print(empty_dict(dict))
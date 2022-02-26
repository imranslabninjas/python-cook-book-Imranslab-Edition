'''
Date : 22 / 2 / 2022


1 : Create a Python Dictionary. It can be any dictionary, you can choose to put any data set you want.
'''

# empty
name = {

}
print(type(name))

# integer numbers of dictionary
numbers = {1: 2, 3: 4, 5: 6, 7: 8, 9: 200, 40000: 546736}
print(type(numbers))

my_infor = {
    "name": "hira",
    "id": 123,
    "hobby": "jump",

}
print(my_infor)
print("\n")

'''
Date  : 24 / 2 /2022
2 : Create a python dictionary with keys of type integer and values of string type.
 What is a dictionary in Python? How is it different from List?
'''

number_info = {
    '1': "Name",
    '2': "Id",
    '3': 'Phone number',
    '4': 'Address',

}
print(number_info)

'''
what is - A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
'''

List = """List is a collection of index values pairs as that of array in c++.
List is created by placing elements in [ ] separated by commas “, “
The indices of list are integers starting from 0.
A list is an ordered sequence of objects """
print(List)

Dictionary = """
Dictionary is a hashed structure of key and value pairs.
Dictionary is created by placing elements in { } as “key”:”value”, each key value pair is separated by commas “, “
The keys of dictionary can be of any data type.
The dictionaries are unordered sets
"""
print(Dictionary)
print("\n")

'''
3 : Suppose, Ross from Friends got married three times in a ten years long TV series, whereas, two times were with the same girl, he does not even know how this happened. But, those, who are like us, watched the show and know how that happened. Suppose, Ross’s sister Monica who is a person with Obsessive Compulsive Disorder, OCD in short, keeps all her data in a dictionary type variable in her secret Python code base hidden somewhere in her parents' house. All her friends got married once, so she never needed to update the dictionary data, Ross made a mess, now she needs to create a new piece of short Python code to handle change in the value for the key 'numberOfDivorce' in her dictionary, she needs to write a define/ method/ function which takes a dictionary as one of the argument, followed by another integer argument of numberOfDivorce data. The 'numberOfDivorce' is supposed to replace the 'numberOfDivorce' with the new one. You can assume the value of the key 'numberOfDivorce'is integer by default. Can you help Monica? Are you making any other assumptions? If yes, let us know how critically you can think.
Monica could just write the following:
Def updateAgeInPersonDictionary(personDictionary, numberOfDivorce):
	# Some Magic Happens here, which you need to help Monica with
	return personDictionary
Test Case:
personDictionary will like this in Input
person = {
    'firstname': 'Ross',
    'lastname': 'Gellar',
    'numberOfDivorce': 1
}
Expected Result:
personDictionary is supposed to change to the following:
person = {
    'firstname': 'Ross',
    'lastname': 'Gellar',
    'numberOfDivorce': 3
}

'''

person ={
    'firstname': 'Ross',
    'lastname': 'Gellar',
    'numberOfDivorce': 1
}

person['numberOfDivorce'] = 3
print(person)
print('\n')

'''
at this time if i want change the key in dictionary ?  
'''
# Example
elements = {"a": 1, "B": 2, "C": 3}

new_element = "apple"
old_element = "a"

elements[new_element] = elements.pop(old_element)

print(elements, "\n")


'''
4 : Suppose you are a teacher’s assistant of the great Physics Professor Richard Feynmann. 
Your job is to maintain a Dictionary, where the key is the roll number of your student
and the value is his/ her assignment marks. A new student got admitted,
you did not know about him/ her until you found an extra assignment to grade on.
Write a Python program, which will take a dictionary as an input argument and an integer as a key and 
another integer as a value. The function/ define/ method will return a dictionary with the new key 
value pair added to the dictionary. Sir Richard Feynmann is one of the most respected professors
in the world of Physics, he was best known for his String theory and the capability to 
make another person understand any difficult and complicated topic. Now, help his TA,
make sure to add proper docstrings, explaining why and what you are doing in your piece of code.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}


'''
sample = {0: 10, 1: 20}
sample.update({2: 30})
print(sample)

# one way - Getting the items from a dictionary key-value pairs in the dictionary.
a_dictionary = {
    "name": "hira",
    "id": 123,
    "hobby": "jump",
}

dict_items = a_dictionary.items()

first_one = list(dict_items)[:1]
print(first_one)

first_two = list(dict_items)[:2]
print(first_two)

first_three = list(dict_items)[:3]
print(first_three)


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
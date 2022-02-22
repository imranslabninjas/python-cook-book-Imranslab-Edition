'''
Date : 22 / 2 / 2022


1 : Create a Python Dictionary. It can be any dictionary, you can choose to put any data set you want.
'''

# empty
name = {

}
print(type(name))

# integer numbers of dictionary

numbers = {1 : 2, 3: 4, 5: 6, 7: 8, 9: 200, 40000: 546736}
print(type(numbers))

my_infor ={
    "name": "hira",
    "id": 123,
    "hobby": "jump",

}
print(my_infor)
print("\n")


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

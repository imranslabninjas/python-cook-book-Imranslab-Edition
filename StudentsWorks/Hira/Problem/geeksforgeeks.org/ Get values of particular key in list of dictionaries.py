'''
Sometimes, we may require a way in which we have to get all the values of specific key
from a list of dictionary.
This kind of problem has a lot of application in web development domain in which
we sometimes have a json and require just to get single column from records.
Let’s discuss certain ways in which this problem can be solved.

Method #1 : Using list comprehension
Using list comprehension is quite straight forward method to perform this particular task.
In this, we just iterate over the list of dictionary for desired value.

'''

# Python3 code to demonstrate working of
# Get values of particular key in list of dictionaries
# Using list comprehension

# initializing list
test_list = [{'gfg': 1, 'is': 2, 'good': 3},
             {'gfg': 2}, {'best': 3, 'gfg': 4}]

# printing original list
print("The original list is : " + str(test_list))

# Using list comprehension
# Get values of particular key in list of dictionaries
res = [sub['gfg'] for sub in test_list]

# printing result
print("The values corresponding to key : " + str(res))

print("\n 2nd method \n")

'''
Method #2 : Using map() + itemgetter()
This problem can also be solved using another technique using map() and itemgetter(). In this,
map is used to link the value to all the dictionary keys and itemgetter gets the desired key.


'''
# Python3 code to demonstrate working of
# Get values of particular key in list of dictionaries
# Using map() + itemgetter()
from operator import itemgetter

# initializing list
test_list = [{'gfg': 1, 'is': 2, 'good': 3},
             {'gfg': 2}, {'best': 3, 'gfg': 4}]

# printing original list
print("The original list is : " + str(test_list))

# Using map() + itemgetter()
# Get values of particular key in list of dictionaries
res = list(map(itemgetter('gfg'), test_list))

# printing result
print("The values corresponding to key : " + str(res))

'''
my won practice using python Using list comprehension.
'''

print("\nmy won practice using python Using list comprehension")
'''
car = [{'1': "tesla", "2": "audi", "3": "Lexue"},
       {"4": "lamborghini", "5": "BMw", "6": "volvo"},
       {'7': "tesla", "8": "audi", "9": "volvo"},
       {'10': "tesla", "11": "audi", "12": "volvo"}

       ]'''
# car1 = [{"tesla": 1, "audi": 2, "Lexue": 3},
#         #{"lamborghini": 4, "BMw": 5, "volvo": 6},
#         {"tesla": 7, "audi": 8, "volvo": 9},
#         {"tesla": 10, "volvo": 11, "audi": 12, "volvo": 13}  #
#
#         ]
# car1 = [{"tesla": 1, 'audi': 2, 'Lexue': 3},
#
#         {"tesla": 10, 'volvo': 11, 'audi': 12, 'volvo': 13}  # {"lamborghini": 4, "BMw": 5, "volvo": 6},
#         # {"tesla": 7, "audi": 8, "volvo": 9},

#      ]
# car1 = [{'gfg': 1, 'is': 2, 'good': 3},
# {'gfg': 2}, {'best': 3, 'gfg': 4}]

car1 = [{"volvo": 11, "audi": 12, "volvo": 13},
        {"volvo": 9},
        {"volvo": 13}  # #{"lamborghini": 4, "BMw": 5, "volvo": 6},
        # {"tesla": 7, "audi": 8,

        ]

print("The original list is : " + str(car1))

car1_number = [sub["volvo"] for sub in car1]
# car1_number = list(map(itemgetter('tesla'), car1))

print(str(car1_number))

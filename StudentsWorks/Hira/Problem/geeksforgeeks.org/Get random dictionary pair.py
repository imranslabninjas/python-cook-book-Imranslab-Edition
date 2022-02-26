'''
Date : 26 / 2 /2022
https://www.geeksforgeeks.org/python-get-random-dictionary-pair/
Python | Get random dictionary pair

Sometimes, while working with dictionaries, we can have a situation in which
we need to find a random pair from the dictionary. This type of problem can come in games such as lotteries etc.
Let’s discuss certain ways in which this task can be performed.
কখনও কখনও, অভিধানগুলির সাথে কাজ করার সময়, আমাদের এমন একটি পরিস্থিতি হতে পারে যেখানে আমাদের
অভিধান থেকে একটি এলোমেলো জোড়া খুঁজে বের করতে হবে। লটারি ইত্যাদির মতো গেমগুলিতে এই ধরনের সমস্যা আসতে পারে৷
আসুন কিছু উপায় নিয়ে আলোচনা করি যার মাধ্যমে এই কাজটি করা যেতে পারে৷



'''

# Python3 code to demonstrate working of
# Get random dictionary pair in dictionary
# Using random.choice() + list() + items()
import random

# Initialize dictionary
test_dict = {'Gfg': 1, 'is': 2, 'best': 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Get random dictionary pair in dictionary
# Using random.choice() + list() + items()
res = key, val = random.choice(list(test_dict.items()))

# printing result
print("The random pair is : " + str(res))
print("\n")

# my practice

import random

# create a new dict
car = {'1': "tesla", "2": "audi", "3": "Lexue", "4": "lamborghini", "5": "BMw", "6": "volvo"}

print("This is my car collection ", str(car))
# converted dict into list and random method using
collections = key, value = random.choice(list(car.items()))
print(" the random pair is ", str(collections))

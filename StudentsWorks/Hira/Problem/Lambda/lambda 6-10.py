'''
Date : 3/8/2022

6. Write a Python program to square and cube every number in a given list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Square every number of the said list:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube every number of the said list:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

'''
# wrong way
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num)
square_num = list(filter(lambda x: x ^ 2, num))  # don't use the filter method  && ^ don't
print(square_num)

'''
This is wright way 
'''

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nSquare every number of the said list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
print("\nCube every number of the said list:")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)

'''
Write a Python program to find whether a given string starts with a given character using Lambda.


'''
starts_with = lambda x: True if x.startswith('P') else False
# print(starts_with('python'))
starts_with = lambda x: True if x.startswith('P') else False
# print(starts_with('java'))

# x.startswith is a method
# case-sensitive
# only find out first word

text = lambda x: x.startswith('w')
print(text("wow"))

text1 = lambda x: True if x.startswith('o') else False
print(text1("oiiiiii"))

print("\n")
'''
Write a Python program to extract year, month, date and time using Lambda.



'''

import datetime

now1 = datetime.datetime.now()  # why datetime 2nd time
print(now1)
thisyear = lambda x: x.year  # thisyear is a  variable
thismonth = lambda x: x.month
thisday = lambda x: x.day
thist = lambda x: x.time()
print(thisyear(now1))
print(thismonth(now1))
print(thisday(now1))
print(thist(now1))

nowTime = datetime.datetime.now()  # this are mathods

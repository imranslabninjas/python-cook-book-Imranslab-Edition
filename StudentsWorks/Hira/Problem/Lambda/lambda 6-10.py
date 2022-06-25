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
7 . Write a Python program to find whether a given string starts with a given character using Lambda.


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
8 . Write a Python program to extract year, month, date and time using Lambda.



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

'''
9. Write a Python program to check whether a given string is number or not using Lambda. Go to the editor
Sample Output:
True
True
False
True
False
True
Print checking numbers:
True
True

aita korbo na cz aiter dorker nai 

'''

is_num = lambda q: q.replace('.', '', 1).isdigit() # why '.' '' 1 ?
print(is_num('26587'))
print(is_num('4.2365'))
print(is_num('-12547'))
print(is_num('00'))
print(is_num('A001'))
print(is_num('001'))
print("\nPrint checking numbers:")
is_num1 = lambda r: is_num(r[1:]) if r[0] == '-' else is_num(r)
print(is_num1('-16.4'))
print(is_num1('-24587.11'))

'''
onther way  takes input value 
'''

# Doesn't work for floats
text = input("Input a word or numbers: ")
if text.isdigit():
    print("The input value is numbers.")
else:
    print("The input value is string.")

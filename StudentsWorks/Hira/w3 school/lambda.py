''''
3/3/2022
Python Lambda
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

'''
#
# b = lambda a: a + 4
# print(b(2))  # a= 2
#
# numbers = lambda a, v, b1, e, r, k: a + v + b1 + e + r + k
# print(numbers(1, 2, 3, 4, 5, 3))

'''
1. Write a Python program to create a lambda function that adds 15 to a given number
 passed in as an argument, also create a lambda function
 that multiplies argument x with argument y and print the result
'''
a = lambda b: b + 15

print("1st part : ", a(10))

num = lambda x, y: x * y
print("2nd part : ", num(12, 4))



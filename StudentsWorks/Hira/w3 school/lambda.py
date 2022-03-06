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

'''
Date: 3/6/2022
Write a Python program to create a function that takes one argument,
and that argument will be multiplied with an unknown given number.

'''


def func_compute(n):
    return lambda x: x * n


result = func_compute(2)
print("Double the number of 15 =", result(15))
result = func_compute(3)
print("Triple the number of 15 =", result(15))
result = func_compute(4)
print("Quadruple the number of 15 =", result(15))
result = func_compute(5)
print("Quintuple the number 15 =", result(15))


def counter_number(n):
    return lambda x: x * n  # new Things is learned  lambda function can be return without passing a variable mane


new_result = counter_number(2)  # n = 2
print(new_result(3))  # here is x = 3


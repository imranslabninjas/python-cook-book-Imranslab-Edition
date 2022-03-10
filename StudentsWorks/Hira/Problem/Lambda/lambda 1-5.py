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

'''
3. Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

'''

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:", subject_marks)

subject_marks.sort(key=lambda x: x[1])
print(subject_marks)

'''
4 Write a Python program to sort a list of dictionaries using Lambda.


'''
models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print("Original list of dictionaries :", models)

new_models = sorted(models, key=lambda x: x['color'])
give_make = sorted(models, key=lambda x: x['make'])
print(new_models)
print(give_make)

'''
5. Write a Python program to filter a list of integers using Lambda. 
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, 898, 2000, 200555, 5]
print(numbers)
even_number = list(filter(lambda X: X % 2 == 0, numbers))
print(even_number)

odd_number = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_number)

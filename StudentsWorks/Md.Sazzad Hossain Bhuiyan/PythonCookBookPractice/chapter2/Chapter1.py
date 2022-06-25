# Chapter 1: Date Structures and Algorithms
# Class 9
# Instructor: Imranul Islam
# Date February 06, 2022
# (C) imranslab 2021-2022 under MIT License
# The company is not liable for any error in code, used for academic purpose only


# Class Exercise 1

# 1.1 Unpacking a Sequence into Separate Variables

# Problem: You have an N-element tuple or sequence that you would like to unpack into a collection of N variables

# a = (4, 5)  # -> Any sequence (or iterable) can be unpacked into variables using simple assignment operation
# x, y = a  # The only requirement is that the number of variables and structure match the sequence
#
# print(x)  # Printing the value of x according to the structure
# print(y)  # Printing the value of y according to the structure

# data = ['ACME', 50, 91.1, (2022, 2, 5)]  # We are putting different data types in each bucket.
#
# # Look closely, you are storing String, int, float, some new kind of structure with a bunch of ints inside
# # Isn't it convenient to write in such format, Try in Java and Kotlin, it's different
# # Food for thought? how do we implement the same concept in Java, JavaScript? I am sure it is differnt? Challenge C?
#
# name, shares, price, date = data
#
# print("name : " + str(name))        # Sneaking into the variable name
# print("shares : " + str(shares))    # Pikabo shares
# print("price : " + str(price))      # Hello price :p
# print("date : " + str(date))        # Hey date?!

# If there is a mismatch in the number of elements, you will get an error. For example:
# Anyone is free to add comments, try Bengali? what happens? does it work? - brain tease?
# Doesn't it look more like natural language? Does it?

# a = (4, 5)
#
# x, y, z = a
# Do you see a red line under idea
# You will get a value error: need more than 2 value

# s = 'Hello'
# a, b, c, d, e = s
#
# # Print on screen, Next time try logging into a file by system time
#
# print("a : " + a)
# print("b : " + b)
# print("c : " + c)
# print("d : " + d)
# print("e : " + e)

# s = 'Hello'
# a, b, c, d, e = s
# print(a)

# When unpacking, you may sometimes want to  discard certain values. Python has no special syntax for this, but you ca
# often just pick a throwaway variable name for it.

# data = ['ACME', 50, 91.1, (2022, 12, 21)]
# G, shares, price,_ = data
#
# print(G)
# print(shares)
# print(price)
# print( _)

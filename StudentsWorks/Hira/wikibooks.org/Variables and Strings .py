'''
https://en.wikibooks.org/wiki/Python_Programming/Variables_and_Strings#Combining_Numbers_and_Strings
Date : 17 / 2 / 2022
Python Programming/Variables and Strings

'''

# red = 5
# blue = 10
# print(red, blue)
# # 5 10
#
# yellow = red
# print(yellow, red, blue)
# # 5 5 10
#
# red = blue
# print(yellow, red, blue)
# # 5 10 10
#
# '''
# wrong way
# red = green
# print(green)
# To understand this code,
# keep in mind that the name of the variable is always on the left side of the equals sign
# (the assignment operator),
# and the value of the variable on the right side of the equals sign. First the name, then the value
# '''
#
# green = red
# print("Now the code number of green number  - ", green)
# print(yellow, red, green, blue)
# '''
# Python knows you want to include the quotation marks in the string, instead of ending the string there.
# '''
# print("So I said, \"You don't know me! You'll never understand me!\"")
#
# '''
# You can add two strings together using the + operator: this is called concatenating them.
# '''
# print("Hello, " + "world!")
#
# '''
# You can also repeat strings by using the * operator, like so:
# '''
# print("bouncy " * 5)
# # bouncy bouncy bouncy bouncy bouncy
# print("bouncy " * 10)
# # bouncy bouncy bouncy bouncy bouncy bouncy bouncy bouncy
# # The string bouncy gets repeated 5 times in the 1st example and 10 times in the 2nd.
#
# '''
# If you want to find out how long a string is, you use the len() function,
# which simply takes a string and counts the number of characters in it.
#  (len stands for "length.") Just put the string that you want to find the
#  length of inside the parentheses of the function. For example:
# '''
# print(len("python just wow"))
#
# # Variables can store much more than just numbers. You can also use them to store strings! Here's how:
# question = "What did you have for lunch?"
# print("question")
# '''
# To ask the user to write something, we used a function called input(), which waits until the user
# writes something and presses enter, and then returns what the user wrote. Don't forget the parentheses!
# '''
# # question = "What did you have for lunch?"
# # print(question)
# # answer = input()
# #
# # print("You had " + answer + "! That sounds delicious!")
#
#
# # Q = 'what is your name '
# # print(Q)
# # Q = input()
# # print('Hi ' + Q + ' how are you')
#
# '''Python is telling us that there is a TypeError,which means there is a problem with the types of
# information being used. Python can't figure out how to reconcile the two types of data that are being used
# simultaneously( means at the same time / together): integers and strings. For example,
# Python thinks that the number variable is holding a string, instead of a number.
# If the user enters 15, then number will contain a string that is two characters long: 1,
# followed by  5. So how can we tell Python that 15 should be a number, instead of a string?
#
# print("Please give me a number: ")
# number = input()
# plusTen = number1 + 10
# print ("If we add 10 to your number, we get " +  plusTen)
#
# Luckily, there are two functions that are perfect solutions for these problems.
# The int() function will take a string and turn it into an integer, while the str() function will take an integer
# and turn it into a string. In both cases, we put what we want to change inside the parentheses
# '''
#
# '''
# print("Please give me a number: ")
# number = input()
#
# number1 = int(number)  # int() function will take a string and turn it into an integer
# plusTen = number1 + 10
# print("If we add 10 to your number, we get " + str(plusTen))
#
# # 2nd
#
# print("Please give me a number:")
# response = input()
#
# number = int(response)
# plusTen = number + 10
#
# print("If we add 10 to your number, we get ", plusTen)  # here , is solved the problem
#
# '''
#
#
# # 3rd
#
# print("Please give me a number:")
# response = input()
# number = int(response)
# plusTen = number + 10
# plusTwenty = number + 20
# print("If we add 10 and 20 to your number, we get %s and %s" % (plusTen, plusTwenty))

# number = int(input("Type in a number: "))
# doubled = number * 2
# print(doubled)

'''
 Write a program that asks the user to type in a string, and then tells the user how long that string was.
'''

# user = input("please type a string : ")
# print (len(user))

# user1 = input("type your name : ")
# print('The string is', len(user1), ' characters long')

'''
Ask the user for a string, and then for a number. Print out that string, that many times.
(For example, if the string is hello and the number is 3 you should print out hello hello hello .)
'''
userString2 = str(input("write some string :"))
# number = 2 * userString2
# print(userString2 + number)

#2nd way
userString = str(input("write some string :"))
use_number = int(input('what number you want : '))

print(userString * use_number)



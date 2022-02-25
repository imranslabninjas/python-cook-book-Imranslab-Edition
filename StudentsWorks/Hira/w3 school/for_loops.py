'''
Python For Loops
Date- 25 /2/2022
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).



'''

# fruits = ['apple', 'green_Apple', 'red_Apple']
# for fruit in fruits:
#     print(fruit)

# Looping Through a String
text = " my name is hira"
text2 = "wo"
text3 = "miko"
for texts in text:            # texts =" "
    for texts2 in text2:       # texts2 = [(w),(o)]
        for texts3 in text3:
            print(texts3)       # texts3 = [(m i k o),(m i k o)]
            print(text)          # " my name is hira"(4)," my name is hira"(4),"wo" "miko"
    print(text2)
    print(text3)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     # print(x) #output comes : apple banana
#     if x == "banana":
#         break
#     print(x)
#     # output comes : apple
#     print("\n")
# '''
# (((The continue Statement)))
# With the continue statement we can stop """the current iteration""" of the loop, and continue with the next:
# '''
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         continue # Do not print banana
#     print(x)

'''
fruits = ['apple', 'green_Apple', 'red_Apple']
for fruit in fruits:
    print(fruit)
    #print(fruits)
# output:
# ['apple', 'green_Apple', 'red_Apple']
# ['apple', 'green_Apple', 'red_Apple']
# ['apple', 'green_Apple', 'red_Apple']
    #print(fruit)
    
******* so many magic here happen *****    
'''

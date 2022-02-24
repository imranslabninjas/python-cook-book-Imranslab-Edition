""" 32 : Generic operations. Run interactive tests to answer the following questions:
a. What happens when you try to use the + operator on different/mixed types
(e.g., string+ list, list + tuple)?
b. Does + work when one of the operands is a dictionary?
Does the append method work for both lists and strings? How about using the keys method on lists?
(Hint: What does append assume about its subject object?)
c. d. Finally, what type of object do you get back when you slice or concatenate two lists or two strings?

"""
s = "Apple"
list1 = ["mango", "banana", "dragon", "orange", "goava"]
str1 = ", "
str2 = " * "

# print(s +" "+ str1.join(list1))
# print(s +" "+ str2.join(list1))
# print(s +" "+ "# ".join(list1))

list2 = [1, 2, 3, 4, 5, 6, 7]
list2 = [str(element) for element in list2]

print(s + " , ".join(list2))




# ranks = list(range(2, 11)) + ['j', 'k', 'q', 'a']
# ranks = [str(rank) for rank in ranks]
# print (ranks)
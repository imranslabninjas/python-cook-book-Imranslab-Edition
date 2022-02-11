# Python list

print("This is the list and it is buli-in data type ")

myList = ["python","java","c","c++" ,"javaScript"]
print(myList)
print("list Allow Duplicates")
myListDuplicates =["python","java","c","c++" ,"javaScript","python","java","c","c++" ,"javaScript"]
print(myListDuplicates)
#how many items a list has?
print("List Length - use the len() function:")
print(len(myListDuplicates))

print("List items can be of any data type")
myListItems=["book",2,6000,"apple",True, False]
print(type(myListItems))

#type()
# From Python's perspective, lists are defined as objects with the data type 'list':
#<class 'list'>

print("What is the data type of a list?")
mylist2 = ["apple", "banana", "cherry"]
print("here i am write only sting ",type(mylist2))

mylist3 =[44,55,2,1,6]
print("number also " ,type(mylist3))

#The list() Constructor
#It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
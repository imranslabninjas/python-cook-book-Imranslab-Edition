# from re import I
# from unittest import result


# l = []
# a = l
# # Adding Element into list
# l.append(5)
# l.append(10)
# print("Adding 5 and 10 in list", l)

# # Popping Elements from list
# a.pop(0)
# print("Popped one element from list", a)
# print("Popped one element from list", l)
# # print()
# # Dictionary
# d = {}

# # Adding the key value pair
# d['five'] = 5
# d["Ten"] =10
# print("Dictionary", d)

# # Removing key-value pair
# del d["Ten"]
# print("Dictionary", d)
# msg = 'hello world'


# number = 100
# i = 0
# result = 0 
# while i < number:
#     result = result + i
#     i+=1
# print(result)

list = [10,12,13,15,25,30,35]
i = 0  
while i<len(list):
    # print(list[i])
    if list[i]==15:
        print(i)
    i += 1

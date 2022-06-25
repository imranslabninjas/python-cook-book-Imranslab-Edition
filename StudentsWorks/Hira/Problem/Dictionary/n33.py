# import random
# dict1 = {1: "Moslin Punjabi", 2: "Jamdani Punjabi", 3: "Banarasi Punjabi"}
# dict2 = {1: "half raincoat", 2: "raincoat with attached umbrella", 3: "Big Umbrella"}
# dict3 = {1: "jacket", 2: "semi light winter jacket", 3: "light winter jacket"}
# dict4 = {1: "Punjabi", 2: "Jamdani", 3: "Banarasi"}
# dict5 = {1: "Muslin", 2: "taat", 3: "bootik"}
# dict6 = {1: "Shirts", 2: "Pants", 3: "Shorts"}
#
# def dict_list(*new_dicts):
#     new_dict_to_send = {1: " ", 2: " ", 3: " " }
#     if len(new_dicts) == 3:
#         var1 = random.randrange(1, 3, 1)
#         for new_dict in new_dicts:
#             for each_element in new_dict_to_send:
#                 if new_dict_to_send[each_element] == " ":
#                     new_dict_to_send[each_element] = new_dict[var1]
#     else:
#         print("you have not entered six elements")
#     return new_dict_to_send
#
# print(dict_list(dict1 , dict2, dict3))

# Python3 code to demonstrate working of
# Get random dictionary pair in dictionary
# Using random.choice() + list() + items()
# import random
#
# # Initialize dictionary
# test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}
#
# # printing original dictionary
# print("The original dictionary is : " + str(test_dict))
#
# # Get random dictionary pair in dictionary
# # Using random.choice() + list() + items()
# res = key, val = random.choice(list(test_dict.items()))
#
# # printing result
# print("The random pair is : " + str(res))






# Python3 code to demonstrate working of
# Get random dictionary pair in dictionary
# Using popitem()

# Initialize dictionary
test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Get random dictionary pair in dictionary
# Using popitem()
res = test_dict.popitem()

# printing result
print("The random pair is : " + str(res))




"""33. Gucci, the cat who has just won the most handsome cat award from Anjelina Jolie. Gucci is known for his fashion sense. Gucci’s human mom is very organised,
she makes Gucci wear clothing according to seasons. As her human mom is a Software Engineer at imranslab, she is supposed to be insane like her coworkers.
She puts too much attention to detail which is one of the important skills any Engineer needs.
She loves the Python Dictionary and prefers using it anywhere she finds. She created 6 dictionaries representing six seasons of Bangladesh. Each dictionary saves the key as the nth day of
 the season and returns the name of the clothing accordingly. Gucci’s human mom is smart and automated the whole process so that she does not have to worry about it in the future.
GrishmoClothing = [1: “Moslin Punjabi”, 2: “Jamdani Punjabi”, 3: “Banarasi Punjabi”, 4: “Taat Punjabi”, … ]
BorshaClothing = [1: ‘half raincoat’, 2: ‘raincoat with attached umbrella’, 3: ‘Big Umbrella’, 4, ‘full raincoat’, … ]
WinterClothing = [1: ‘light winter jacket’, 2: ‘semi light winter jacket’, 3: ‘semi light winter jacket with one orange inner’, 4: ‘winter jacket’, 5: ‘heavy duty winter jacket’,
 6 : ‘winter jacket with wool inner’, …]
Gucci is travelling to Mars by Elon Musk’s Starship. The rocket fare is high and lets you carry very small luggage as carry on. She can carry a maximum
 of 6 clothes but she is confused about what to take.
Write a Python Program, which will take 6 dictionaries as arguments and returns a dictionary of 6 items where 1 item was selected randomly from each dictionary.
It is to make sure Gucci can survive artificial weather created on Mars by Nuclear explosions on the north and south poles of the planet. The explosion helped Mars
create an artificial customizable weather which helped create a mini Bangladesh on Mars and the weather is just like home. Please assume the number of days for a year
on Mars equals that of earth in this approximate calculation.
"""


import random

dict1 = {1: "Moslin Punjabi", 2: "Jamdani Punjabi", 3: "Banarasi Punjabi"}
dict2 = {1: "half raincoat", 2: "raincoat with attached umbrella", 3: "Big Umbrella"}
dict3 = {1: "jacket", 2: "semi light winter jacket", 3: "light winter jacket"}
dict4 = {1: "Punjabi", 2: "Jamdani", 3: "Banarasi"}
dict5 = {1: "Muslin", 2: "taat", 3: "bootik"}
dict6 = {1: "Shirts", 2: "Pants", 3: "Shorts"}


def dict_list(*new_dicts):
    list_of_new_dicts = list(new_dicts)
    new_dict_to_send = {}
    keys = [0, 1, 2, 3, 4, 5]
    if len(new_dicts) == 6:
        # var1 = random.randrange(1, 4, 1)
        for each_element in keys:
            for new_dict in new_dicts:
                if new_dict == list_of_new_dicts[each_element]:
                    var1 = random.randrange(1, 4, 1)
                    new_dict_to_send[each_element + 1] = new_dict[var1]
    else:
        print("You haven't entered six elements")
    return new_dict_to_send



print(dict_list(dict1, dict2, dict3, dict4, dict5, dict6))

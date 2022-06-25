""" Suppose, you are a scientist at NASA. You were supposed to make a dictionary which was supposed to have the city as
one of the keys. The city key is a string with a value of String stored against it. But your product manager understood his mistake,
he thinks location would be a better word if used instead of city.It happened because, most of the employees joining NASA are not from cities
anymore but also in sub urban areas. Location will make the data more accurate.
Write a program to rename a key “city” to a “ location”  in the following dictionary.
sample_dict = {
  "name": "John F. Kennedy",
  "age":70,
  "salary": 80000,
  "city": "Chittagong"
}

"""

sample_dict = {
    "name": "John F. Kennedy",
    "age": 70,
    "salary": 80000,
    "city": "Chittagong"
}

sample_dict_2 = {
    "name": "obama",
    "age": 60,
    "salary": 90000,
    "city": "Dhaka"
}
sample_dict_3 = {
    "name": "Trump",
    "age": 85,
    "salary": 30000,
    "city": "Uganda"
}
sample_dict_4 = {
    "name": "Biden",
    "age": 85,
    "salary": 100000,
    "city": "W.Dc"
}

sample_list = [sample_dict, sample_dict_2, sample_dict_3, sample_dict_4]


def rename_key(sample_dict_to_change):
    if sample_dict_to_change.keys().__contains__("city"):
        sample_dict_to_change["location"] = sample_dict_to_change.pop("city")
    return sample_dict_to_change


def a(list_of_dicts):
    """ a() method will modify key of dictionaries and returns modified list of dictionaries """
    new_list_of_dicts = []
    for dict in list_of_dicts:
        new_list_of_dicts.append(rename_key(dict))

    return list_of_dicts


print(rename_key(sample_dict))

print(a(sample_list))

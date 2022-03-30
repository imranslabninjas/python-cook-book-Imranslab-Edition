"""Given two string s1 and s2 check if they are anagrams. Two strings are anagrams if they are made of the same
characters with the same frequencies
Example:
    s1 = "danger"
    s2 = "garden"

    output: true
    explanation:
"""


def solution(string1, string2):

    string1 = string1.lower()
    string2 = string2.lower()

    if len(string1) != len(string2):
        return False

    character_frequency_dictionary = {}

    for letter in string1:
        if letter in character_frequency_dictionary:
            character_frequency_dictionary[letter] += 1
        else:
            character_frequency_dictionary[letter] = 1

    for letter in string2:
        if letter in character_frequency_dictionary and character_frequency_dictionary[letter] > 0:
            character_frequency_dictionary[letter] -= 1
        else:
            return False

    if sum(character_frequency_dictionary.values()) == 0:
        return True
    else:
        return False

"""Assuming we can import Counter from collections"""
from collections import Counter
def solution2(string1, string2):
    if len(string1) != len(string2):
        return False

    else:
        string1 = sorted(string1.lower())
        string2 = sorted(string2.lower())

        return Counter(string1) == Counter(string2)


"""Using Sorting function
T(n) = O(nlogn) + o(nlogn) + n
    ~= n
"""
def solution3(string1, string2):
    if len(string1) != len(string2):
        return False

    string1 = string1.lower()
    string2 = string2.lower()

    return sorted(string1) == sorted(string2)


"""Driver Code"""
s1 = "nameless"
s2 = "salesman"
print("The String is :" + str(solution(s1, s2)))
print("The String is :" + str(solution2(s1, s2)))
print("The String is :" + str(solution3(s1, s2)))

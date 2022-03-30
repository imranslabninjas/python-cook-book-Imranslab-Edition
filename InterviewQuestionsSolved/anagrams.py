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
        if letter in character_frequency_dictionary:
            character_frequency_dictionary[letter] -= 1
        else:
            return False

    if sum(character_frequency_dictionary.values()) == 0:
        return True
    else:
        return False


"""Driver Code"""
s1 = "Race"
s2 = "Care"
print("The String is :" + str(solution(s1, s2)))

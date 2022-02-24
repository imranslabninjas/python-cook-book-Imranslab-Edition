'''
5 : Suppose you love Astronomy, you are a big fan of space, you dream to make a space faring civilization.
Somehow, you time travelled. You are living in Sundarban, in 2200 AD. Which is 178 years from today.
In the year 2200, you found that humans can fly to another planet at a speed slightly less than
the speed of light. You came to this new planet, which is far away from our earth.
The size of the planet is super big. The rule of the planet is, if you walk 1 Metre, you win 1m^2 space.
With every metre x m walk you win x * x sq metres as shown in the following dictionary.
Somehow you added an extra entry by error to the end.
Write a Python program, which will have a define/ method/ function, which will take a dictionary as an argument and drop the last key-value pair and return the modified dictionary. Make sure to drop the only last one, others will make a mess of your ownership of that planet. You might get kicked out, which we do not want.
Removing elements from a dictionary

squares = {“1”: 1, “2”: 4, “3”: 9, “4”: 16, “5”: 25}
Expected result:squares = {“1”: 1, “2”: 4, “3”: 9, “4”: 16}
'''
# Answer
squares = {'1': 1, '2': 4, '3': 9, '4': 16, '5': 25}
squares.pop('5')
print(squares)

# other way
print("The popitem() method removes the last inserted item "
      "(in versions before 3.7, a random item is removed instead):")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
print('\n')

print(" pop() method removes the item with the specified key name:")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.pop("model")
print(thisdict)
print('\n')

'''


'''
print("The del keyword removes the item with the specified key name:")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

may = {
    "name": "hira",
    "id": 12,
    "add": "dhaka"
}
del may['id'] # del mathod delete the key
print(may)

may.popitem()
print(may) # this popitem work for the last key

print('\n The clear() keyword empties the dictionary:')
may.clear()
print("This dictionary is empty", may)
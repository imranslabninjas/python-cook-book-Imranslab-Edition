# Slicing
""" You can return a range of characters by using the slice syntax. Specify the start index and the end index,
separated by a colon, to return a part of the string.
we will get the characters from start index to end index(end index not included) """

b = "Hello, World!"
print(b[1:4]) # it will print the characters from position 1 to position 4(position 4 not included)

# Slice From the Start
""" If we do not specify the starting index, it will start from index 0 """
print(b[:5])

# Slice To the End
""" If we do not specify the end index, it will go to the end """
print(b[4:])

# Negative Indexing
"""Use negative indexes to start the slice from the end of the string. index -1 denotes  last of the string,
 index -2 denotes 2nd last of the string and so on"""
b = "Hello World"
# here -1 = d, -2 = l, -3 = r, ...., -11 = H. [-5:-1] means start index -5 and end index -1. so it will print 'Worl'
print(b[-5:-1])
# Slicing
""" You can return a range of characters by using the slice syntax. Specify the start index and the end index,
separated by a colon, to return a part of the string.
we will get the characters from start index to end index(end index not included) """

b = "Hello, World!"
print(b[1:4])  # it will print the characters from position 1 to position 4(position 4 not included)

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

# Modify Strings (Upper Case & Lower Case)
# The upper() method returns the string in upper case:
a = "Hello, World"
print(a.upper(), '\n')

# The lower() method returns the string in lower case:
print(a.lower(), '\n')

# Remove Whitespace
# The strip() method removes any whitespace only from the beginning and the end:
a = " Hello World "
print("using strip function:", a.strip(), '\n')

# To replace all space from the String, use string.replace() function
print("using replace function:", a.replace(" ", ""), '\n')

""" The replace() method replaces a string with another string:
Syntax of Replace function:  string.replace(old, new, count)
old – old substring you want to replace. 
new – new substring which would replace the old substring.
count – the number of times you want to replace the old substring with the new substring. (Optional ) """

a = "Hello World"
print(a.replace('l', ''), '\n')

song = 'Let it be, let it be, let it be, let it be'
print(song.replace('let', "don't let", 2), '\n')  # Think about this output

# Split String
""" The split() method splits the string into substrings if it finds instances of the separator. """
a = "Hello,World!"
b = a.split()  # split() method doesn't find any instance of the separator.
print(b)
b = a.split(',')
print(b, '\n')

a = "Hello World!"
b = a.split()
print(b, '\n')

a = "HelloWorld!"
b = a.split('W')
print(b) # ['Hello', 'orld!'] will be print
b = ' W'.join(a.split('W'))
print(b)  # Hello World! will be print
# Assign String to a Variable
a = 'Hello'
print (a,'\n')

# Multiline Strings

# using three double quotes:
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt."""
print(b,'\n')

# using three single quotes:
b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b,'\n')

# Strings are Arrays
a = 'I Love Bangladesh'
print(a[2],'\n') # at index 2 we will get 'L', beecause array index start from 0.

# Looping Through a String
for x in "Bangladesh":
  print(x)
print('\n')

# String Length
p = 'I Love Bangladesh'
print('length of p: ',len(p),'\n') # The len() function returns the length of a string

# Check String
""" To check if a certain phrase or character is present in a string, we can use the keyword 'in'. 
it will returns Boolean(true/false). """
txt = "I Love Bangladesh"
print("my" in txt," 'my' is not present in txt ")  # it will print False
print("I" in txt," 'I' is present in txt ")  # it will print True

if "Love" in txt:
    print("Yes, 'Love' is present in txt.\n")

# Check if NOT
""" To check if a certain phrase or character is NOT present in a string, we can use the keyword 'not in'. """
print("my" not in txt," 'my' is not present in txt ")  # it will print True
print("I" not in txt," 'I' is present in txt ")  # it will print False

if 'base' not in txt:
    print("No, 'base' is NOT present in txt.")
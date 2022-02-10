# Unpacking a Sequence into Separate Variables
# You have an N-elements tuple or sequence that you would like to unpack into a collection of N variables.

# Example-1

# a = (4, 5, 6)
# x, y, z = a  # this line unpacks values
# print(x)  # x will print 4
# print(y)  # y will print 5
# print(z)  # z will print 6
#
# # k, m = a    # error: too many values to unpack (expected 2)
# # print(k)
# # print(m)
#
# # b, c, d, e = a   # ValueError: not enough values to unpack (expected 4, got 3)
# # print(b)
# # print(c)
# # print(d)
# # print(e)
#
# # Example-2

# data = ['xyz', 40, (13, 2, 1982), 'Teaching']
# name, age, DOB, profession = data
# d, m, y = DOB
# # name, age, (d, m, y), profession = data
# print('Name:', name)
# print('date of birth:', DOB)
# print('profession:', profession)
# print('day', d)
# print('month', m)
# print('year', y)

# Example-3

# Unpacking actually works with any object that happens to be iterable, not just tuples or lists
s = 'hello world'
a, b, c, d, e, f, g, h, i, j, k = s
print(a)
print('f:', f)  # this will print space between 'hello' and 'world'
print(k)

# Example-4

# you may sometimes want to discard certain values. Python has no
# special syntax for this, but you can often just pick a throwaway variable name for it.

data = ['xyz', 40, (13, 2, 1982), 'Teaching']
name, p, p, profession = data  # 40 will be discarded
print(name)
print(profession)
print(p)
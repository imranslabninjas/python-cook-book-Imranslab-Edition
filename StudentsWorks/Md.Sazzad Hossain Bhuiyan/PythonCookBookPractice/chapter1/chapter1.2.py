""" Unpacking Elements from Iterables of Arbitrary Length
You need to unpack N elements from an iterable, but the iterable may be longer than N elements.

Example-1  """

data = ('ACME', 50, 123.45, (12, 18, 2012), 'ImransLab')

""" last two elements will be assigned to y and z Respectively and
 remaining will be assigned to x """
*x, y, z = data

print('x', x)
print('y', y)
print('z', z)
print('\n')
""" first element will be assigned to x, last element will be assigned to z
 and remaining will be assigned to y """
x, *y, z = data

print('x', x)
print('y', y)
print('z', z)
print('\n')

""" first two elements will be assigned to x and y Respectively and
 remaining will be assigned to z """
x, y, *z = data

print('x', x)
print('y', y)
print('z', z)
print('\n')

# Example-2 (Unpacking Using normal function)

records1 = [
('foo', 1, 2),
('bar', 'hello'),
('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)
for tag, *args in records1:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
print('\n')

# Example-3  (Unpacking Using Lambda Expression)

records = [('A', 1, 2.03), ('B', 'hello'), ('a', 3, 4)]
record1 = lambda x, y: print('A', x, y)
record2 = lambda x: print('B', x)
record3 = lambda x, y: print('a', x, y)
for i, *j in records:
    """ python is a case-sensitive language. 'A' and 'a' is not equal.So, line No 9 is not true for record3 """
    if i == 'A':
        record1(*j)
    elif i == 'B':
        record2(*j)
    else:
        record3(*j)
# record = ('ACME', 50, 123.45, (12, 18, 19, 2012))
# name, *_, (*__, year) = record
#
# print(name)
# print(*_)
# print(*__)
# print(year)

record = \
    [
        ("jam", 1, 3.01),
        ("jelly", 1, 2),
        ("jam", 2, 7.43),
    ]

def do_foo(x, y):
    print('jam', x, y)


def do_bar(s, a):
    print('jelly', s)

for tag, *args in record:
    if tag == "jam":
        do_foo(*args)
    elif tag == "jelly":
        do_bar(*args)

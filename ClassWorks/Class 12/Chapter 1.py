record = \
    [
        ("Siyam", 1, 3.01),
        ("Habibullah", 1, 2),
        ("Siyam", 2, 7.43),
    ]

def do_foo(x, y):
    print('Siyam', x, y)


def do_bar(s, a):
    print('Habibullah', s)

for tag, *args in record:
    if tag == "Siyam":
        do_foo(*args)
    elif tag == "Habibullah":
        do_bar(*args)

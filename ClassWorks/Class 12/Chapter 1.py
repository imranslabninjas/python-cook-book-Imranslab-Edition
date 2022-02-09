record = [
    ("Siyam", 1, 3.01),  # Element 1
    ("Habibullah", 1),  # Element 2
    ("Siyam", 2, 7.43), ]  # Element 3


def do_foo(x, y):
    print('Siyam', x, y)


def do_bar(s):
    print('Habibullah', s)


for tag, *args in record:
    if tag == "Siyam":
        do_foo(*args)
    elif tag == "Habibullah":
        do_bar(*args)

x = 31
y = 12
z = 2099

a = int(input("Enter the day"))
b = int(input("Enter the month"))
c = int(input("Enter the year"))

if c > z:
    print("The year should be smaller than 2099")
elif b == 1 and a > 31:
    print("This month can't be longer than 31 days.")
elif b == 3 and a > 31:
    print("This month can't be longer than 31 days.")
elif b == 4 and a > 30:
    print("This month can't be longer than 30 days.")
elif b == 5 and a > 31:
    print("This month can't be longer than 31 days.")
elif b == 6 and a > 30:
    print("This month can't be longer than 30 days.")
elif b == 7 and a > 31:
    print("This month can't be longer than 31 days.")
elif b == 8 and a > 31:
    print("This month can't be longer than 31 days")
elif b == 9 and a > 30:
    print("This month can't be longer than 30 days")
elif b == 10 and a > 30:
    print("This month can't be longer than 31 days")
elif b == 11 and a > 30:
    print("This month can't be longer than 30 days")
elif b == 12 and a > 31:
    print("This month can't be longer than 31 days")
elif b == 2 and a > 28 and c % 4 != 0:
    print("This month can't be longer than 28 days")
elif b == 2 and a > 28 and c % 4 == 0 and c % 400 == 0:
    print("This month can't be longer than 28 days")
elif b == 2 and a > 29:
    print("This month can't be longer than 28 days")
else:
    i = 0
    p = 0
    q = 0
    r = 0
    for i in range(c, 2099):
        if i % 4 == 0 and i % 400 == 0:
            p = p + 365
        elif i % 4 == 0 and i % 400 != 0:
            p = p + 366
        else:
            p = p + 365

    if b == 3:
        q = 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 31 - a
    elif b == 4:
        q = 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 30 - a
    elif b == 5:
        q = 30 + 31 + 31 + 30 + 31 + 30 + 31 + 31 - a
    elif b == 6:
        q = 31 + 31 + 30 + 31 + 30 + 31 + 30 - a
    elif b == 7:
        q = 31 + 30 + 31 + 30 + 31 + 31 - a
    elif b == 8:
        q = 30 + 31 + 30 + 31 + 31 - a
    elif b == 9:
        q = 31 + 30 + 31 + 30 - a
    elif b == 10:
        q = 30 + 31 + 31 - a
    elif b == 11:
        q = 31 + 30 - a
    elif b == 12:
        q = 31 - a
    elif b == 2:
        if c % 4 == 0 and c % 400 == 0:
            q = 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31 - a
        elif i % 4 == 0 and i % 400 != 0:
            q = 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 29 + 31 - a
        else:
            q = 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31 - a
    elif b == 1:
        if c % 4 == 0 and c % 400 == 0:
            q = 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31 - a
        elif i % 4 == 0 and i % 400 != 0:
            q = 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 29 + 31 + 31 - a
        else:
            q = 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 - a
    else:
        print("Enter month correctly")
        # break

    r = p + q
    if r % 7 == 0:
        print("The day is Thursday")
    elif r % 7 == 1:
        print("The day is Wednesday")
    elif r % 7 == 2:
        print("The day is Tuesday")
    elif r % 7 == 3:
        print("The day is Monday")
    elif r % 7 == 4:
        print("The day is Sunday")
    elif r % 7 == 5:
        print("The day is Saturday")
    elif r % 7 == 6:
        print("The day is Friday")
    print(r)

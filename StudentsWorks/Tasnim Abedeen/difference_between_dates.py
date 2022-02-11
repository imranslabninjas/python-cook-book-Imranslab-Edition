# This programme will find the difference between dates using if elif else function
# The earlyest date should be entered first

a = int(input("enter starting day:"))
b = int(input("enter starting month:"))
c = int(input("enter starting year:"))
d = int(input("enter ending day:"))
e = int(input("enter ending month:"))
f = int(input("enter ending year:"))

if a > d:  # if a is bigger than d. That means the day to be subtracted is larger. So extra 31,30,29 or 28
    # days will be added based on which month it is being subtracted from
    if e == 1:
        p = d + 31 - a
    elif e == 2:
        p = d + 31 - a
    elif e == 4:
        p = d + 31 - a
    elif e == 6:
        p = d + 31 - a
    elif e == 9:
        p = d + 31 - a
    elif e == 11:
        p = d + 31 - a
    elif e == 3:  # calculating weather leap year or mot
        if f % 4 == 0 and f % 400 == 0:
            p = d + 28 - a
        elif f % 4 == 0 and f % 400 != 0:
            p = d + 29 - a
        else:
            p = d + 28 - a
    else:
        p = d + 30 - a
    e = e - 1   # extra month should be subtracted
else:
    p = d - a

if b > e:
    q = e + 12 - b
    f = f - 1
else:
    q = e - b

r = f - c

print("excluding the starting date, the difference is", p, "days", q, "months and", r, "years")
print("including the starting date, the difference is", p + 1, "days", q, "months and", r, "years")

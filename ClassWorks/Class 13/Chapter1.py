# record = ('ACME', 50, 123.45, (12, 18, 19, 2012))
# name, *__, (*__, year) = record
#
# print(name)
# print(*__)
# print(*__)
# print(year)

# number = 1
#
# def addTwoToNumber(number):
#     number = number+number
#     print(number)
#
#     addTwoToNumber(number)
#
# addTwoToNumber(number)

items = [1, 10, 7, 4, 5, 9]
head, *tail = items


# print(head)
# print(*tail)

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


sum(items)

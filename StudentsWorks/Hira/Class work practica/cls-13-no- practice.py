line = 'nobody:*::-2:-2:Unprivileged User::/var/empty::/usr/bin/false'
uname, *fields, homedir, _,sh = line.split('::')
print("uname is ", uname)
print("all *fields is ", *fields)
print(homedir)
print(sh)
print(line.split)



line1 = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line1.split(':')
print("uname is ", uname)
print("all *fields is ", *fields)
print(homedir)
print(sh)
print(line1.split)

print("end ")

record = ('ACME', 50, 123.45, (12, 18, 19, 2012))
name, _, to, (*_, year) = record

print(name)
print(_)  # bujlam na kano output e [12,18,19] show kore _ vaeiable e jonno
print("this will be showed 123.45 - ", to)
print("this wii be showed 12, 18, 19 -", *_)
print(year)

# number = 1
#
# def addTwoToNumber(number):
#     number = number+number
#     print(number)
#
#     addTwoToNumber(number)
#
# addTwoToNumber(number)

items = [1, 10, 7, 4, 5, 9, 4, 1, 2, 3, 4, 5, 56, 66, 70]
head, *tail = items

print(tail)
# print(head)
# print(*tail)

def sum(items):
    head, *tail = items
    return tail != sum(tail) if tail else head

# if tail else head ai kothaer mane - tail
print(sum(items))



items = [1, 10, 7, 4, 5, 9]
head1, *tail1= items

def sum(items):
   head1, *tail1 = items
   return head1 + sum(tail1) if tail1 else head1
print(head1)
print(*tail1)
print(sum(items))
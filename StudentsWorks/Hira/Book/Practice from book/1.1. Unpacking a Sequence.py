#problem --

# You have an N-element tuple or sequence that you would like to unpack into a collection
# of N variables.

# example for tuple which is bult-in data type

#1st
car = ["volvo", "bmw"]
x, y = car
print(x)
print(y)
#this is wrong code
# number = (2, 4, 7, 9, 10)
# number = x, a, v, b, n
# print(x)
# print(a)

#15 number line e age jodi variable k declar or daki tahole kaj korbe na cz
# valu gula k ami number name akta variable er rakchi akhon sob value k aber akta akta name dichi
# then oi  name diye oigula k print korly value paoh jabe .kinto ai jaiya aita hoyse na .

# this is right code
number = (2, 24, 7, 9, 10)
x, a, v, b, n = number
print(x)
print(a)

p = (4, 5)
x, y = p
print(y)

# 2nd
data = ["Hafiz", 14, 4, (7, 7, 2009)]
name, age, idNumber, date = data
print("Id Number - ", idNumber)
print("Person Name - ", name)

#This is wrong way
# name, age, idNumber, date, (day, month,year) = data
# print("Birthday Day number - ", day)

#39 number line vul,
# date aita r likha jabe na,
# cz not enough values to unpack
# date jonno r value nai
# (day, month,year) er maje aage date chole gese .

#This is right way.

info = ["Hasib", 20, 78787, 1908908989, (14, 7, 2002)]
name, age, idNumber, phoneNumber, (day, month, year) = info
print(phoneNumber)

#Unpacking actually works with any object that happens to be iterable, not just tuples or
#lists. This includes strings, files, iterators, and generators. For example:

a ="Hira"
z, x, c, vee = a
print(vee)
print(c)
print(x)
print(z)

#When unpacking, you may sometimes want to discard certain values. Python has no
#special syntax for this, but you can often just pick a throwaway variable name for it. For

#আপনি কখনও কখনও কিছু মান বাতিল করতে চাইতে পারেন .
#kiso value k ami bad dite cay ai jonno paython onno kono way nai .aktai way holo je "same name deoh"
# tahole pora valuta python nibe . aita k bole "value override" kora
#example:
# data = ['ACME', 50, 91.1, (2012, 12, 21) ]
# _, shares, price, _ = data
# print(shares)
# print( _)

name = ['hafiz', 'hira', 'hasib', 'English-book', 'python-book']
a, _, p, _, _, = name
print(_)
print(_)
print(_)
print(_)
print(a)
print(p)

#ai vabe ami hafiz and enlish book aita  remove kore dite pari ..
# and ber ber jodi same value dey ai python book aitai pabo.

name = ['hafiz', 'hira', 'hasib', 'English-book', 'python-book']
a, getout, p, getout, getout, = name
print(getout)
print(a)
print(p)
print(getout)















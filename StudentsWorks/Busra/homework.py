#Task 1
txt = "Imranslab is the best!"
for line in range(3):
    result = txt
    print(result)

#Task 2- Don't know how to solve it.

#Task 3
x = 23/6
print(int(x))

#Task 4
y = "I\'m a student"
print(y)

#Task 5 - confused with this one
a = "Hello"
b = 5
c = 35.65
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Task 6
import keyword
print(keyword.kwlist)

#Task 7 - how do u do that like task 6?
print("Numbers (like 0-9) is not allowed in the first place of a variable name.\nHyphen and spaces are not allowed in the middle of a variable name. ")

#Task 8
p = """Hello there!
This is a multiline string.
Enjoy programming!"""
print(p)

#Task 9 - maybe this is how you do it?
e = 9
print(e==9)
print(e<=9)
print(e>=9)
print(e!=9)
print(e<9)
print(e>9)
#Task 10 -confused
f = ((10<5) and (4<5))
print(f)
#When we use the 'and' operator both of the relation has to be correct for it to print a true boolean value.

g = ((10>5) and (3>2))
print(g)

h = ((10>5) or (5<4))
print(h)

i = ((10<5) or (6<3))
print(i)

j = 56
j = (not (j==56))
print(j)

k = "Hello"
k = (not (k!="Hello"))
print(k)

#Task 11

a1 = 2
b1 = 3
a1 +=b1
print(a1)

a2 = 5
a2 -=2
print(a2)

a3 = 8
a3 *=2
print(a3)

a4 = 4
a4 /=4
print(int(a4))

a5 = 5
a5 **=2
print(a5)

a6 = 4
a6 %=3
print(a6)

a7 = 44
a7 //=2
print(a7)

#Task 12 don't know how to do that
amit_age = 19
farhan_age = 18


def my_func():
    if (amit_age or farhan_age) >= 18:
        print("Eligible")
    else:
        print("Not eligible")

my_func()

#Task 13
number = int(input())
def number_function():
    if number %2==0:
      print("Even")
    else: print("Odd")
number_function()

"""
This is a multiline comment. 
"""
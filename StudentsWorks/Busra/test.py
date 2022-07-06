import keyword
print(keyword.kwlist)
print("Hi")

x = "Python, is, great, right?"
y = x.split(",")

print(y)

print("Hello There")

box1 = ("Watch")
print(box1)

number = [2,4,5,6,9]
a,b,c,d,e = number
print(a)

"""
Hi
"""
x = 1
print("x=1")

x=1
x=2
print(x)

y = 2
y **=2
print(y)

number = 8

if number<4:
    print("positive")
else:
    print("neg")

print(f"{number} is true")

answer = int(input('What is the answer to 1+2?'))
def equation(answer):
    if answer == 3:
        print ('Correct!')
    else:
        print ('Wrong, it is 3!')
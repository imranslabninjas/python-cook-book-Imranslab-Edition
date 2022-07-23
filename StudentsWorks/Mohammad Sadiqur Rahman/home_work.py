#01. write about imranslab one time and print it 3 times?
for i in range(0,3):
    i = "It is an online platform to learn Python."
    print(i)
print("\n")

#2.bring (512.0) this result by using only the multiline operator and (2,2,3)only this number?
number = (2**3)**3
print(number)
print("\n")

#3. (23/6)in this code add only one operator to get output 3? and (3.0 or Something) is not acceptable?
result = 23/6
print(int(result))
print("\n")

#4. I'm a student-print this?
message = "I'am a student."
print(message)
print("\n")

#5. create different variables (like string, float, integer, bool, etc) then put their value then print them?
string_variable = "Hello world."
print(string_variable)
float_variable = 4.75
print(float_variable)
integer_variable = 100
print(integer_variable)
bool_variable = True
print(bool_variable)
print("\n")

#6. print all the reserved keys of python.
import keyword
print(keyword.kwlist)
print("Total number of keywords is: " , len(keyword.kwlist))
print("\n")

#7. print all characters that are not allowed as a variable name in the first position?
#8. write a multiline string and print it?
message_on_variable = "Variable names can contain only letters, numbers and underscores. \
                        They can start with a letter or an underscore, but not with a number.\
                        Spaces are not allowed in variable names but underscore can be used \
                        to separate words in variable."
print(message_on_variable)
print("\n")

#9. write all comparison operators and print them as true or false?
'''Less than ( < )         Less than or equal to ( <= )
    Greater than ( > )      Greater than or equal to ( >= )
    Equal to ( == )         Not equal to ( != ) '''
print(19 < 17)
print(18 <= 18)
print(34 > 54)
print(23 >= 25)
print(40 == 40)
print (32 != 32)
print("\n")

#10. print true or false using and, or, not operator?
print(19 > 17 and 18 <= 18)
print(34 > 54) or (23 <= 25)
print(not(19 >= 20))
print(not(40 >= 40 or 23 <= 25))
print("\n")

#11. write some assignment operators and print them?
'''
Assign ( = )                        Add and Assign ( += )           Subtract and Assign ( -= )
Multiply and Assign ( *= )          Divide and Assign ( /= )        Modulus and Assign ( %= )
Divide (floor) and Assign ( //= )   Exponent and Assign ( **= )     Bitwise AND and Assign ( &= )
Bitwise OR and Assign ( |= )        Bitwise XOR and Assign ( ^= )   Bitwise Right Shift and Assign ( >>= )
Bitwise Left Shift and Assign ( <<= )
'''
x = 5
y = 3
x = y
print(x)
a = 5
b = 3
a += y
print(a)
c = 5
d = 3
c -= d
print(c)
e = 5
f = 3
e *= f
print(e)
g = 5
h = 3
g /= h
print(g)
i = 5
j = 3
i %= j
print(i)
k = 5
l = 3
k //= l
print(k)
l = 5
m = 3
l **= m
print(l)
n = 5
p = 3
n &= p
print(n)
q = 5
r = 3
q |= r
print(q)
s = 5
t = 3
s ^= t
print(s)
u = 5
v = 3
u >>= v
print(u)
w = 5
z = 3
w <<= h
print(w)
print("\n")

#12. Program to check whether a person is eligible to vote or not.?
age = input("Enter your age: ")
age = int(age)
if age >= 18:
    print("Now, cast your vote.")
else:
    print("Sorry, you are too young for vote.")
print("\n")

#13. Program to check whether a number is even or not.
number = input("Enter a number : ")
number = int(number)
if number % 2 == 0:
    print(number, " is an even number.")
else:
    print(number,  " is an odd number.")
print("\n")

#14. describe all code using single comment and multiline comment
    # This is an example of a single comment.
'''
    Multiple comments are used to comment 
    more than one line at a time. It is a good practice to add comment 
    in program.
'''

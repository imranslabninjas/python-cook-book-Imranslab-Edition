# print("Please enter your age so that we can calculate if you are a senior citizen?")
# age = float(input())
#
# if age >= 60.0:
#     print("You are a Senior citizen")
#
# elif age < 60.0:
#     print("You are not senior citizen")
from audioop import avg


class Actor:
    def __init__(self, name, age, *movies):
        self.name = name
        self.age = age
        self.movies = movies

    def addAge(self, age):
        self.age = self.age + age

#
# # making Object 1
# p1 = Actor("Shahrukh Khan", 60, "Koala", "DDLJ", "Kuch kuch hota hain", "Kabhi Khushi Kabhi Gum")
#
#
# # making Object 2
# p2 = Actor("Salman Khan", 55, "Kick", "Daban", "Ek tha tiger", "Sultan", "Body guard", "Dabang")
#
# # printing Object 1 information
# print("My name is :" + p1.name)
# print("My name is :" + str(p1.age))
# print("Movies of " + p1.name +" is :"+ str(p1.movies))
#
# # printing Object 1 information
# print("My name is :" + p2.name)
# print("Movies of " + p2.name +" is :"+ str(p2.movies))
#
# p1.addAge(10)
# p1.addAge(20)
#
# # printing Object 1 information
# print("My name is :" + p1.name)
# print("My name is :" + str(p1.age))
#
# # printing Object 1 information
# print("My name is :" + p2.name)
# print("My name is :" + str(p2.age))


class Student:
    def __init__(self, name, date_of_birth, max_degree_obtained, *marks):
        self.name = name
        self.date_of_birth = date_of_birth
        self.max_degree_obtained = max_degree_obtained
        self.marks = marks

    def average_marks(self, *marks):
        return (sum(marks)/ len(marks))


sazzad = Student("Sazzad", "1995-01-01", "PhD", 10, 10, 10 ,10, 10)
hira = Student("Anny Hira", "2008-01-01", "SSC", 10, 11, 9, 10, 12)
Siyam = Student("Siyam", "1991-01-01", "Post Doc", 9, 11, 12, 12, 14)
Sobuz = Student("Sobuz", "1992-01-01", "PhD", 9, 11, 12, 11, 12)
Sadikur = Student("Sadikur", "1993-01-01", "Master", 9, 11, 12, 10, 10)

string1 = "Average marks for the student "

print(string1 + sazzad.name + " is " + sazzad.average_marks())



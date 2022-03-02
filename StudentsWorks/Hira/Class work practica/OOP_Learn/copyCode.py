
class Actor:
    def __init__(self, name, age, *movies):
        self.name = name
        self.age = age
        self.movies = movies

    def addAge(self, age):
        self.age = self.age + age


# making Object 1
p1 = Actor("Shahrukh Khan", 60, "Koala", "DDLJ", "Kuch kuch hota hain", "Kabhi Khushi Kabhi Gum")


# making Object 2
p2 = Actor("Salman Khan", 55, "Kick", "Daban", "Ek tha tiger", "Sultan", "Body guard", "Dabang")

# printing Object 1 information
print("My name is :" + p1.name)
print("My name is :" + str(p1.age))
print("Movies of " + p1.name +" is :"+ str(p1.movies))

# printing Object 1 information
print("My name is :" + p2.name)
print("Movies of " + p2.name +" is :"+ str(p2.movies))

p1.addAge(10)
p1.addAge(20)

# printing Object 1 information
print("My name is :" + p1.name)
print("My name is :" + str(p1.age))

# printing Object 1 information
print("My name is :" + p2.name)
print("My name is :" + str(p2.age))



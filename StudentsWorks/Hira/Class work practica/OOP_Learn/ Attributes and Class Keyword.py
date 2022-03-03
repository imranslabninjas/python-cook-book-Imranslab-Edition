# myList = [1, 2, 3, 4, 5]
# print(type(myList))
#
# myset = set()  # this set create me that's means -  we can create our won user defined  object . python allows us
# print(type(myset))
# print(type(myList))
#
#
# class actor():
#     pass # don't do anything

class actor():
    def __init__(self, name, idNo, height, wight, *likeItems):
        self.takeName = name
        self.takeIdNo = idNo
        self.takeHeight = height
        self.takeWight = wight
        self.takeLikeItems = likeItems


# make object for 1 person
person1 = actor('hira', 2, 5.3, '50kg', "mlik", "foods", "Biriyani", "cake", "pudding", "chips", "biscutes")

print("the person1 name is :", person1.takeName)
print("the person 1 id no is :", person1.takeIdNo)
print("the person1 height is :", person1.takeHeight)
print("the person 1 id wight is :", person1.takeWight)
print("the person1 lisk items is :", person1.takeLikeItems)

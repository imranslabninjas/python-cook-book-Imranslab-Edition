students = []
sec_name = []
second_low = 0
n = int(input("Input number of students: "))
for _ in range(n): # - jokhon variablee name use korra lagbe na tokhon .
    s_name = input("Name: ")
    score = float(input("Grade: "))
    students.append([s_name, score])
print("\nNames and Grades of all students:")
print(students)
order = sorted(students, key=lambda x: int(-[1]))
for i in range(n):
    if order[i][1] != order[0][1]:
        second_low = order[i][1]
        break
print("\nSecond lowest grade: ", second_low)
sec_student_name = [x[0] for x in order if x[1] == second_low]
sec_student_name.sort()
print("\nNames:")
for s_name in sec_student_name:
    print(s_name)

# 17 .Write a Python program to find palindromes in a given list of strings using Lambda.
texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
print("Orginal list of strings:")
print(texts)
result = list(filter(lambda x: (x == "".join(reversed(x))), texts))
print("\nList of palindromes:")
print(result)

txt =['hih', "aba", "cg"]
#number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202]
print(txt)
found = list(filter(lambda x: (x == "".join(reversed(x))), txt))
print(found)


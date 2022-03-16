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

from collections import deque

q = deque(maxlen=2)
q.append(1)
q.append(2)
q.append(3)
# q.insert(4, 1)  # (9,1 ) output = 4 number position e 9 no value nose and array print kore,
# q.insert(0, 8)                    # ami mone kore chilam je pore jodi 4,5,6 amon position e value deoh hoy tahole sey
#                                   # vabei hobe but ta hoy nai .ami aita buji nai.
# q.insert(7, 0)                    # ami bujte perechi . deque er 2 side e holo valure jete pare ,
#                                   # so je value jabe just oita bose jabe laste and frist
# q.insert(0,12)
# q.insert(1,15)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)
q.append(6)
print(q)  # deque([2, 3, 4, 5, 6], maxlen =5) 1 number remove .
# if i cahnge my max length . see whats happend
# output get only 5,6 when i append 6


q.appendleft(200)
print(q)

number = [22, 43, 56, 11]
number.pop(3)  # index number
print(number)

num1 = [33, 44, 1, 4]
num1.pop(1)
# num1.popleft() # kaj korbe na cz  aita aage ami deque method likhi nai .
print(num1)

rol = deque([10, 20, 30], maxlen=20)
# rol.append([2,4,3,5])
# print(rol)
# popleft
rol.popleft()
print(rol)

c = deque([4, 1, 2])
c.popleft()
print(c)

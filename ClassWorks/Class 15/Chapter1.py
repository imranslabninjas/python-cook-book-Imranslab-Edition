# We will be learning little more about deque.
# Analogy of Deque
from collections import deque

q = deque(maxlen=5)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
print(q)

# Guess what will happen if we add another element to the deque?
# We have set the maximum length of the deque to be 5. Is it going to interfere?
# What this parameter will do?

q.append(6)
q.append(7)
print(q)

# Observer, is append function adding to the front or to the back?

q.appendleft(1)
q.appendleft(2)

# Is this left, left of you? or the left of screen? Think?
print(q)

# What is pop. What is the meaning of popping something? Any analogy?
pop1 = q.pop()
pop2 = q.pop()
pop3 = q.pop()

print(pop1)
print(pop2)
print(pop3)

# What happens to the deque after popping
print(q)

# Why did it shrink? So, what is popping
# Does it pop from right or from left?
# How do we pop from the other side, is it possible? yes/ no/ very good

pop1 = q.popleft()
pop2 = q.popleft()

print(pop1)
print(pop2)

print(q)

# Do you notice the order? Why is it like that? analogy, appreciated!

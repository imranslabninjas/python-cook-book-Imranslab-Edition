# # We will be learning little more about deque.
# # Analogy of Deque
# from collections import deque
#
# q = deque(maxlen=5)
# q.append(1)
# q.append(2)
# q.append(3)
# q.append(4)
# q.append(5)
# # print(q)
#
# # Guess what will happen if we add another element to the deque?
# # We have set the maximum length of the deque to be 5. Is it going to interfere?
# # What this parameter will do?
# #
# q.append(6)
# q.append(7)
# print(q)
# #
# # # Observer, is append function adding to the front or to the back?
# #
# q.appendleft(1)
# q.appendleft(2)
# #
# # # Is this left, left of you? or the left of screen? Think?
# print(q)
# #
# # What is pop. What is the meaning of popping something? Any analogy?
# pop1 = q.pop()
# pop2 = q.pop()
# pop3 = q.pop()
#
# print(pop1)
# print(pop2)
# print(pop3)
# #
# # # What happens to the deque after popping
# print(q)
# #
# # # Why did it shrink? So, what is popping
# # # Does it pop from right or from left?
# # # How do we pop from the other side, is it possible? yes/ no/ very good
# #
# pop1 = q.popleft()
# pop2 = q.popleft()
# #
# print(pop1)
# print(pop2)
# #
# print(q)
#
# # Do you notice the order? Why is it like that? analogy, appreciated!
#
'''
Lambda Expression and introduction to functional programming
What is Lambda Expression: It can also be called anonymous function
Can a function be anonymous? Until whatever we learnt
function can be anonymous and it can be used for sorting and filtering
Recommended video: https://www.youtube.com/watch?v=25ovCm9jKfA

lambda argument(s) : expression
'''
# add5 = lambda x: x + 5
# print(add5(90))

# square = lambda x: x * x
# print(square(7))

# division5 = lambda x: x // 5  # What is the difference between / and //?
# print(division5(12))
#
# division6 = lambda x: x/6
# print(division6(36))
#
# '''
# Let us try to make Lambda Functions with more than one arguments
# lambda arguments : expression
# '''
# addab = lambda a, b: a + b
# print(addab(2, 3))
#
# '''
# Should we try setting a default value of any variable inside the lambda function? Lets see what happens
# '''
#
addab = lambda a=8, b=9: a + b
# print(addab())  # Try it without using () after the function name i.e. print(addab), What do you see? Think! - Google?

print(addab(1, 2))
#
# '''
# We will learn little bit about heap data structure in this course, we wont go into too much detail.
# We will just touch the surface.
# Recommended video: https://www.youtube.com/watch?v=hkyzcLkmoBY
# '''

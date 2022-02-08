''' Unpacking Elements from Iterables of Arbitrary Length Today I learnt: the thriple ' thing can help make multiline
comment output

*** Problem: ***
You need to unpack N elements from an iterable, but the iterable may be longer than N
elements, causing a ...

*** Solution: ***
Python "Star expressions" can be used to address this problem. For example, suppose you
run a course and decide at the end of the semester that you're going to drop the first and last homework grades,
and only average the rest of them. If there are only four assignments, maybe you simply unpack all four, but what if
there are 24? A star expression makes it easy: '''

# from audioop import avg

''' 
No idea why did I even import this module
'''

#
# def drop_first_last(grades):
#     first, middle, last = grades
#     return avg(middle)


'''
As another use case, suppose you have user records that consist of a name and email address, followed by an arbitrary 
number of phone numbers. You could unpack the records like this:
'''

# record = ('Elon Musk', 'elonmusk@elonmusk.elonmusk', '0171xxxxxxxx..', '0181xxxxxxxxx', '01911xxxxxxxxxxxx', '0167123456789')
# name, email, *phone_numbers = record
#
# print(name)
# print(email)
# print(*phone_numbers)

'''It's worth nothing that the phone_numbers variable will always be a list, regardless of how many phone numbers are 
unpacked including none. Thus, any code that uses phone_numbers won't have to account for the possibility tht it 
might not be a list or perform any kind of additional type checking. 

The starred variable can also be the first one in the list. For example, say you have a sequence of values 
representing your company's sales figures for the last eight quarters. If you want to see how the most recent quarter 
stacks up to the average of the first seven, you could do something like this: '''

sales_record = [1, 8, 9, 7, 6, 5, 4, 3, 2, 1]
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
'''See documentation for the sum function, how is it working?'''
print(trailing_avg)
# return avg_comparison(trailing_avg, current_qtr)

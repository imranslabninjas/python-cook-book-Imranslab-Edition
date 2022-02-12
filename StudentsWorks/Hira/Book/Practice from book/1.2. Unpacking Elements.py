# Chapter 1: Date Structures and Algorithms
# Date February 12, 2022
#used for academic purpose only
print("1.2. Unpacking Elements from Iterables of Arbitrary Length")

from audioop import avg

''' 
No idea why did I even import this module
'''

grades = [1, 3, 6, 2, 6, 9]
def drop_first_last(grades):
    first, *middle, last = grades
    _avg = sum(middle) / len(middle)
    return _avg
print("avg: ", drop_first_last(grades))


sales_record = [1, 8, 9, 7, 6, 5, 4, 3, 2, 1, 3, 4, 10, 12, 11]
*trailing_sales, current_qtr = sales_record
trailing_avg = sum(trailing_sales) / len(trailing_sales)
'''See documentation for the sum function, how is it working?'''
print(trailing_avg)

sales_record2 = [1, 8, 9, 7, 6, 5, 4, 3, 2, 1, 3, 4, 10, 12, 11]
*allRecode, currentRecord = sales_record2
recodeAvg = sum(allRecode) / len(allRecode)
print(recodeAvg)


'''
As another use case, suppose you have user records that consist of a name and email
address, followed by an arbitrary number of phone numbers. You could unpack the
records like this:
'''
import heapq

numbers = [1, 2, 4, 0, 2, 6, 17, 19, 25, -1, -2, -3, 41, 42, 43, 55, 65, 75, 85]

print(heapq.nlargest(3, numbers))
print(heapq.nsmallest(3, numbers))

'''
Lets use some more weird data and more complicated data to sort
'''
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 10},
    {'name': 'FB', 'shares': 80, 'price': 20},
    {'name': 'Intel', 'shares': 90, 'price': 5},
    {'name': 'Qualcomm', 'shares': 110, 'price': 50},
    {'name': 'AMD', 'shares': 120, 'price': 40},
    {'name': 'Microsoft', 'shares': 10, 'price': 60},
    {'name': 'Oracle', 'shares': 200, 'price': 100},
]

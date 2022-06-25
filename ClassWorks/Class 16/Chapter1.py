import heapq
# #
# # numbers = [1, 2, 4, 0, 2, 6, 17, 19, 25, -1, -2, -3, 41, 42, 43, 55, 65, 75, 85]
# #
# # print(heapq.nlargest(10, numbers))
# # print(heapq.nsmallest(10, numbers))
#
# # '''
# # Lets use some more weird data and more complicated data to sort
# # '''
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 10},
    {'name': 'FB', 'shares': 80, 'price': 20},
    {'name': 'Intel', 'shares': 90, 'price': 5},
    {'name': 'Qualcomm', 'shares': 110, 'price': 70},
    {'name': 'AMD', 'shares': 120, 'price': 40},
    {'name': 'Microsoft', 'shares': 10, 'price': 60},
    {'name': 'Oracle', 'shares': 200, 'price': 100},
]
# # '''
# # Cheapest and most expensive shares from a complicated data structure
# # '''
# # cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
# #
# # print(cheap)
# # print(expensive)
# #
# # '''
# # Minimum and maximum number of shares from a complicated data structure
# # '''
# #
# # minNumberShares = heapq.nsmallest(3, portfolio, key=lambda s: s['shares'])
# # maxNumberShares = heapq.nlargest(3, portfolio, key=lambda s: s['shares'])
# #
# # print(minNumberShares)
# # print(maxNumberShares)


A = list(range(1, 10))
B = list(range(10))
C = list(range(10))
M = []
for a in A:
    for b in B:
        for c in C:
          N= 100*a+10*b+c
if (N % 3) == 2:
  M.append(N)
W = M[0]
for i in range(2, len(M)+1):
  W = W+M[i+1]
print(W)
# https://github.com/BexTuychiev/medium_stories/tree/master/2021/august/4_manim_basics

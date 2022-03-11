'''
Date : 22/023/11
11 . Write a Python program to find intersection of two given arrays using Lambda.


'''

array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]
print("Original arrays:")
print(array_nums1)
print(array_nums2)
result = list(filter(lambda x: x in array_nums1, array_nums2))
print("\nIntersection of the said arrays: ", result)

'''
12. Rearrange positive and negative numbers in a given array using Lambda
'''
array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
print("Original arrays:")
print(array_nums)
result = sorted(array_nums, key=lambda i: 0 if i == 0 else -1 / i)
print("\nRearrange positive and negative numbers of the said array:")
print(result)

'''
13. Write a Python program to count the even, odd numbers in a given array of integers using Lambda
that means fine the lenth
'''

array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
print("Original arrays:")
print(array_nums)
odd_ctr = len(list(filter(lambda x: (x % 2 != 0), array_nums)))
even_ctr = len(list(filter(lambda x: (x % 2 == 0), array_nums)))
print("\nNumber of even numbers in the above array: ", even_ctr)
print("\nNumber of odd numbers in the above array: ", odd_ctr)
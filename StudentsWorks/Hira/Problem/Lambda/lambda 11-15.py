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

# me
s_Id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
s_rool = [2, 3, 4, 5, 6, 7, 11]

result = list(filter(lambda x: x in s_Id, s_rool))
print('\nthe common value', result)

# m2

num1_list = [22, 33, 33, 44, 55, 11, 66, 66, 77, 777, 888, 888]
num2_list = [22, 33, 44, 55, 66, 77, 78, 78, 77, 899, 90]
print('the main list: ', num2_list, num1_list)
list_re = list(filter(lambda v: v in num2_list, num1_list))
print("Hera is the common value:", list_re)

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
that means fine the length
'''

array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
print(array_nums)
odd_ctr = len(list(filter(lambda x: (x % 2 != 0), array_nums)))
even_ctr = len(list(filter(lambda x: (x % 2 == 0), array_nums)))
print("\nNumber of even numbers : ", even_ctr)
print("\nNumber of odd numbers : ", odd_ctr)

# me find evem and odd number length
my_array = [22, 33, 44, 55, 121, 344, 67, 899, 444, 555, 343, 448]
found_even = list(filter(lambda x: x % 2 == 0, my_array))
print('This is only even number', found_even)
found_len_even = len(found_even)
print('Here Length ', found_len_even)

'''
14 .Write a Python program to find the values of length six in a given list using Lambda.


'''
print("\n")
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Hasibb']
days = filter(lambda day: day if len(day) == 6 else '', weekdays)  # here Day in nor a mathod
for d in days:
    print("wow 3 days ", d)

'''
The filter() function returns an iterator were the items are filtered
through a function to test if the item is accepted or not.
filter() ফাংশন একটি পুনরাবৃত্তিকারী প্রদান করে যেখানে
আইটেমটি গৃহীত হয়েছে কিনা তা পরীক্ষা করার জন্য একটি ফাংশনের মাধ্যমে আইটেমগুলি ফিল্টার করা হয়।
'''

'''
15. Write a Python program to add two given lists using map and lambda. Go to the editor
Original list:
[1, 2, 3]
[4, 5, 6]
'''

l1 = [1, 2, 3]
list2 = [4, 5, 6]
adding = map(lambda x, y: x + y, l1, list2)
print(list(adding))

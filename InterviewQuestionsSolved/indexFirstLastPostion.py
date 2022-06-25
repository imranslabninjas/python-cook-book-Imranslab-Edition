"""
Given a sorted array of integers arr and an integer target, find the index of the first and last position of target in
arr. In target can not be found in arr, return [-1, -1]

Example:
    input:
    arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
    target = 5
    output: [2, 6]

Solution is wrong, need to revisit
"""


def solution1(arr, target):
    start = -1
    end = -1
    answer = [start, end]

    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i + 1 < len(arr):
                if arr[i + 1] == target:
                    end = i + 1
                    i += 1
                elif arr[i + 1] != target:
                    return answer
                answer = [start, end]
    return answer


def solution2(arr, target):
    start = get_first_occurance_solution2(arr, target)
    end = get_last_occurance_solution2(arr, target)
    output = [start, end]
    return output


def get_first_occurance_solution2(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def get_last_occurance_solution2(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            while arr[i] == target and i+1 < len(arr):
                if arr[i + 1] != target:
                    return i
                elif i + 1 == len(arr) -1:
                    return i + 1
                i = +1
    return -1


arr = [2, 4, 6, 6, 6, 6, 6, 6, 9, 9]
target = 9

print("Answer :" + str(solution1(arr, target)))
print("Answer :" + str(solution2(arr, target)))

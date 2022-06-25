import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2, 89]
find_lar = heapq.nlargest(1, nums)  # how many
print(find_lar)

# smallest numbers at lest 5
find_sml = heapq.nsmallest(5, nums)
print(find_sml)

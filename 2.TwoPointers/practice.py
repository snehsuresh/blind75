"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

"""

nums = [1, 2, 2, 3, 3, 3]
k = 2


# Heap solution
heap = []
import heapq

res = []
hMap = {}
for i in range(len(nums)):
    hMap[nums[i]] = hMap.get(nums[i], 0) + 1

for key, val in hMap.items():
    heapq.heappush(heap, (-val, key))

while k:
    val, key = heapq.heappop(heap)
    res.append(key)
    k -= 1
print(res)

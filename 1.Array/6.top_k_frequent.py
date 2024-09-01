"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

"""

nums = [1, 2, 2, 2, 2, 2, 2, 3, 3, 3]
k = 2


# =============== brute force ======================
# from collections import defaultdict

# hMap = {}
# for i in range(len(nums)):
#     hMap[nums[i]] = hMap.get(nums[i], 0) + 1

# sorted = sorted(hMap.items(), key=lambda item: item[1], reverse=True)
# print(sorted[:3])


# ================Heap solution ================= klogn
import heapq

freq = {}
for num in nums:
    freq[num] = 1 + freq.get(num, 0)

heap = []
for num, freq in freq.items():
    heapq.heappush(heap, (-freq, num))  # Negate frequency to simulate max-heap

res = []
while heap:
    freq, num = heapq.heappop(heap)
    res.append(num)

# print(res)


# ================Bucket Sort : More Optimized================ n


hMap = {}
for i in range(len(nums)):
    hMap[nums[i]] = hMap.get(nums[i], 0) + 1
freq = [[] for i in range(1, len(nums) + 1)]
# print(freq)

for n, c in hMap.items():
    freq[c].append(n)
res = []
for i in range(len(freq) - 1, 0, -1):
    if len(freq[i]):
        for j in range(len(freq[i])):
            res.append(freq[i][j])
            if len(res) == k:
                print(res)

"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Input: nums = [2,20,4,10,3,4,5]

Output: 4
"""

nums = [2, 20, 4, 10, 3, 4, 5]
# expected = 1
nums.sort()
numSet = set(nums)
maxLen = 1
for num in numSet:
    if len(numSet) == 1:
        print(1)
    if num - 1 in numSet:
        continue
    if num + 1 in numSet:
        curlen = 1
        while (num + curlen) in numSet:
            curlen += 1
    maxLen = max(curlen, maxLen)

print(maxLen)

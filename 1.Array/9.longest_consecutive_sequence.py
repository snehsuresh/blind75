"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Input: nums = [2,20,4,10,3,4,5]

Output: 4
"""

nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
# expected = 1

numSet = set(nums)
start = False
output = 0
for num in numSet:
    # is it the start of a sequence?
    if len(numSet) == 1:
        print(1)
    if num - 1 in numSet:
        continue
    if num + 1 in numSet:
        length = 1
        while num + length in numSet:
            length += 1
        output = max(length, output)
print(output)

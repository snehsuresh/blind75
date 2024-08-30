"""
Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums
except nums[I].
The product of any prefix or suffix of nums is guaranteed to fit in a
32-bit integer.
You must write an algorithm that runs in O(n) time and without
using the division operation.
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""

# Brute Force

nums = [1, 2, 3, 4]
output = []
for i in range(len(nums)):
    res = 1
    for j in range(len(nums)):
        if j != i:
            res *= nums[j]
    output.append(res)


# Pre and Post fix method.
# nums = [1, 2, 3, 4]
nums = [-1, 0, 1, 2, 3]


def apws(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return nums[0]
    output = [1] * len(nums)
    pre = post = 1
    for i in range(len(output)):
        # making prefix
        output[i] *= pre
        pre *= nums[i]

    for i in range(len(output) - 1, -1, -1):
        output[i] *= post
        post *= nums[i]
    print(output)


apws(nums)

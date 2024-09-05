"""
Given an integer array nums, find the subarray with the largest
sum, and return its sum.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum of 1.
"""

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# -------- Brute force:  Cubic solution 3 for loops --------

max_sum = 0
sum = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        sum = 0
        for k in range(i, j + 1):
            sum += nums[k]
        max_sum = max(sum, max_sum)
print(max_sum)

# -------- Quadratic Solution 2 for loops -------------
max_sum = 0
sum = 0
for i in range(len(nums)):
    cur_sum = nums[i]
    for j in range(i + 1, len(nums)):
        cur_sum += nums[j]
        max_sum = max(cur_sum, max_sum)

print(max_sum)


# -------- Linear solution (skip negative numbers) ---------

maxSum = nums[0]
sum = 0
for i in range(len(nums)):
    if sum < 0:
        sum = 0
    sum += nums[i]
    maxSum = max(sum, maxSum)
print(maxSum)

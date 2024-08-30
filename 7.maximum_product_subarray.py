"""
Given an integer array nums, find a subarray that has the largest
product, and return the product.
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a
subarray.
"""

# --- brute force --- Cubic solution

nums = [1, 2, -3, 4]
# expected output 4
max_prod = -1
for i in range(len(nums)):
    for j in range(i, len(nums)):
        prod = 1
        for k in range(i, j + 1):
            if nums[k] == 0:
                prod = 0
                continue
            prod *= nums[k]
        max_prod = max(prod, max_prod)

print(max_prod)


# --- Optimized ---- Quadratic solution
nums = [1, 2, -3, 4]
max_prod = -1
for i in range(len(nums)):
    prod = 1
    for j in range(i, len(nums)):
        if nums[j] == 0:
            prod = 0
            continue
        prod *= nums[j]
    max_prod = max(prod, max_prod)

print(max_prod)


# --- optimized linear time ----
nums = [-2, 0, -1]
start = 0
end = len(nums) - 1
prefix = suffix = 1
maxVal = float("-inf")

while start < len(nums):
    if prefix == 0:
        prefix = 1
    if suffix == 0:
        suffix = 1
    prefix *= nums[start]
    suffix *= nums[end]

    start += 1
    end -= 1

    maxVal = max(prefix, suffix, maxVal)

print(maxVal)

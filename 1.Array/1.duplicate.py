"""
3. Contains Duplicate
Given an integer array nums, return true if any value appears at
least twice in the array, and return false if every element is
distinct.
Input: nums = [1,2,3,1]
Output: true
"""

nums = [1, 2, 3, 1]
hSet = set()


def duplicate():
    for i in range(len(nums)):
        if nums[i] in hSet:
            return True
        hSet.add(nums[i])
    return False


print(duplicate())

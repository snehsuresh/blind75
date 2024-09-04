"""
Given an array of integer nums and an integer target, return
indices of the two numbers such that they add up to the target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""

nums = [1, 2, 3, 4]
target = 3

hMap = {}


def twoSum():
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hMap:
            return [i, hMap[diff]]
        hMap[num] = i
    return False


print(twoSum())

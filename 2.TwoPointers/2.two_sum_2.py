"""
Two Integer Sum II
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target 
and index1 < index2. 
Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.

"""

# We used hMap for twoSum earlier, but that takes more than O(1) space worst case

numbers = [1, 2, 3, 4]
target = 3

start = 0
end = len(numbers) - 1
sum = 0
while start < end:
    sum = numbers[start] + numbers[end]
    if sum < target:
        start += 1
    elif sum > target:
        end -= 1
    if sum == target:
        print(start + 1, end + 1)

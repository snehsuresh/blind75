"""
Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] 
where nums[i] + nums[j] + nums[k] == 0,
and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. 
You may return the output and the triplets in any order.

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
"""

nums = [1, -1, -1, 0]


nums.sort()
res = []
for i in range(len(nums)):
    if nums[i] > 0:
        break
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    start = i + 1
    end = len(nums) - 1

    while start < end:
        threesum = nums[i] + nums[start] + nums[end]
        if threesum < 0:
            start -= 1
        elif threesum > 0:
            end -= 1
        if threesum == 0:
            res.append([nums[start], nums[end], nums[i]])

        start += 1
        end -= 1

        # what if [-2,-2,-2,0,0,0, 2, 2, 2] even if you move pointers, you end up at same numbers
        while start < end and nums[start] == nums[start - 1]:
            start += 1
        while end > start and nums[end] == nums[end + 1]:
            end -= 1
print(res)

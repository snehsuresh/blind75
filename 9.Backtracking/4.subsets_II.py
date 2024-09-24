"""
Subsets II
Solved 
You are given an array nums of integers, which may contain duplicates. 
Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,1]

Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
Example 2:

Input: nums = [7,7]

Output: [[],[7], [7,7]]

REFER PNG FOR [1,2,2,3]
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res


"""
Call Stack Trace:
backtrack(0, [])
backtrack(1, [1])
backtrack(2, [1, 1])
backtrack(3, [1, 1, 2]) → (Base case, add subset)
backtrack(3, [1, 1]) → (Base case, add subset)
backtrack(2, [1]) (i updated to skip duplicate)
backtrack(3, [1, 2]) → (Base case, add subset)
backtrack(3, [1]) → (Base case, add subset)
backtrack(1, []) (i updated to skip duplicate)
backtrack(2, [2])
backtrack(3, [2]) → (Base case, add subset)
backtrack(3, []) → (Base case, add subset)
"""

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [1, 2, 1]
    output1 = solution.subsetsWithDup(nums1)
    print("Subsets for nums = [1, 2, 2, 3]:", output1)

    # Example 2
    nums2 = [7, 7]
    output2 = solution.subsetsWithDup(nums2)
    print("Subsets for nums = [7, 7]:", output2)

"""
Subsets
Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. 
You may return the solution in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [7]

Output: [[],[7]]


"""

from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [1, 2, 3]
    output1 = solution.subsets(nums1)
    print("Subsets for [1, 2, 3]:", output1)

    # Example 2
    nums2 = [7]
    output2 = solution.subsets(nums2)
    print("Subsets for [7]:", output2)

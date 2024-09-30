"""
Combination Target Sum
You are given an array of distinct integers nums and a target integer target. 
Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. 
Two combinations are the same if the frequency of each of the chosen numbers is the same, 
otherwise they are different.

You may return the combinations in any order and the order of the numbers in each 
combination can be in any order.

Example 1:

Input: 
nums = [2,5,6,9] 
target = 9

Output: [[2,2,5],[9]]
Explanation:
2 + 2 + 5 = 9. We use 2 twice, and 5 once.
9 = 9. We use 9 once.

Example 2:

Input: 
nums = [3,4,5]
target = 16

Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]
Example 3:

Input: 
nums = [3]
target = 5

Output: []
"""

from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            curr.append(nums[i])
            dfs(i, total + nums[i])
            curr.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res


"""
Combinations for nums = [2, 3, 6, 7], target = 7

Call stack
dfs(0, [], 0)
    dfs(0, [2], 2)
        dfs(0, [2, 2], 4)
            dfs(0, [2, 2, 2], 6)
                dfs(0, [2, 2, 2, 2], 8) → (Backtrack)
            dfs(1, [2, 2, 2], 6)
                dfs(1, [2, 2, 2, 3], 9) → (Backtrack)
            dfs(2, [2, 2, 2], 6)
                dfs(2, [2, 2, 2, 6], 12) → (Backtrack)
            dfs(3, [2, 2, 2], 6)
                dfs(3, [2, 2, 2, 7], 13) → (Backtrack)
        dfs(1, [2, 2], 4)
            dfs(1, [2, 2, 3], 7) → (Valid combination: [2, 2, 3], Backtrack)
        dfs(2, [2, 2], 4)
            dfs(2, [2, 2, 6], 10) → (Backtrack)
        dfs(3, [2, 2], 4)
            dfs(3, [2, 2, 7], 11) → (Backtrack)
    dfs(1, [2], 2)
        dfs(1, [2, 3], 5)
            dfs(1, [2, 3, 3], 8) → (Backtrack)
        dfs(2, [2, 3], 5)
            dfs(2, [2, 3, 6], 11) → (Backtrack)
        dfs(3, [2, 3], 5)
            dfs(3, [2, 3, 7], 12) → (Backtrack)
    dfs(2, [2], 2)
        dfs(2, [2, 6], 8) → (Backtrack)
    dfs(3, [2], 2)
        dfs(3, [2, 7], 9) → (Backtrack)
dfs(1, [], 0)
    dfs(1, [3], 3)
        dfs(1, [3, 3], 6)
            dfs(1, [3, 3, 3], 9) → (Backtrack)
        dfs(2, [3, 3], 6)
            dfs(2, [3, 3, 6], 12) → (Backtrack)
        dfs(3, [3, 3], 6)
            dfs(3, [3, 3, 7], 13) → (Backtrack)
    dfs(2, [3], 3)
        dfs(2, [3, 6], 9) → (Backtrack)
    dfs(3, [3], 3)
        dfs(3, [3, 7], 10) → (Backtrack)
dfs(2, [], 0)
    dfs(2, [6], 6)
        dfs(2, [6, 6], 12) → (Backtrack)
    dfs(3, [6], 6)
        dfs(3, [6, 7], 13) → (Backtrack)
dfs(3, [], 0)
    dfs(3, [7], 7) → (Valid combination: [7])

"""


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [2, 3, 6, 7]
    target1 = 7
    output1 = solution.combinationSum(nums1, target1)
    print("Combinations for nums = [2, 3, 6, 7], target = 7:", output1)

    # Example 2
    nums2 = [3, 4, 5]
    target2 = 16
    output2 = solution.combinationSum(nums2, target2)
    print("Combinations for nums = [3, 4, 5], target = 16:", output2)

    # Example 3
    nums3 = [3]
    target3 = 5
    output3 = solution.combinationSum(nums3, target3)
    print("Combinations for nums = [3], target = 5:", output3)

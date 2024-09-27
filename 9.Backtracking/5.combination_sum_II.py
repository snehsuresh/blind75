"""
Combination Target Sum II
Solved 
You are given an array of integers candidates, which may contain duplicates, 
and a target integer target. Your task is to return a list of all unique combinations 
of candidates where the chosen numbers sum to target.

Each element from candidates may be chosen at most once within a combination. 
The solution set must not contain duplicate combinations.

You may return the combinations in any order and the order of the 
numbers in each combination can be in any order.

Example 1:

Input: candidates = [9,2,2,4,6,1,5], target = 8

Output: [
  [1,2,5],
  [2,2,4],
  [2,6]
]
Example 2:

Input: candidates = [1,2,3,4,5], target = 7

Output: [
  [1,2,4],
  [2,5],
  [3,4]
]

Problem is a combination of subset 2 and combination sum 1
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, total):
            if i >= len(candidates) or total > target:
                return
            if target == total:
                res.append(curr.copy())
                return
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    candidates1 = [9, 2, 2, 4, 6, 1, 5]
    target1 = 8
    output1 = solution.combinationSum2(candidates1, target1)
    print("Combinations for candidates = [9, 2, 2, 4, 6, 1, 5], target = 8:", output1)

    # Example 2
    candidates2 = [1, 2, 3, 4, 5]
    target2 = 7
    output2 = solution.combinationSum2(candidates2, target2)
    print("Combinations for candidates = [1, 2, 3, 4, 5], target = 7:", output2)

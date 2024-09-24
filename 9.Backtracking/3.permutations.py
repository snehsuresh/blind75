"""
Permutations
Solved 
Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [7]

Output: [[7]]
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return [[]]

        permutations = self.permute(nums[1:])
        res = []
        for perm in permutations:
            for i in range(len(perm) + 1):
                perm_copy = perm.copy()
                perm_copy.insert(i, nums[0])
                res.append(perm_copy)
        return res


"""
Call Stack Trace:
permute([1, 2, 3])
permute([2, 3])
permute([3])
permute([]) → (Base case)
permute([3]) (returns [[]])
permute([2, 3]) (processes perm = [[]])
permute([2, 3]) (returns [[3]])
permute([1, 2, 3]) (processes perm = [[3]])
permute([1, 2, 3]) (processes perm = [[2]])
permute([1, 2, 3]) (processes perm = [[1, 2]])
permute([1, 2, 3]) (returns [[2, 3], [3, 2]])
permute([1, 2, 3]) (processes perm = [[2, 3], [3, 2]])
permute([1, 2, 3]) (processes perm = [[1, 3, 2], [3, 1, 2]])
permute([1, 2, 3]) (returns [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

"""

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [1, 2, 3]
    output1 = solution.permute(nums1)
    print("Permutations for nums = [1, 2, 3]:", output1)

    # Example 2
    nums2 = [7]
    output2 = solution.permute(nums2)
    print("Permutations for nums = [7]:", output2)

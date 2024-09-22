"""
Binary Tree Maximum Path Sum
Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

Example 1:



Input: root = [1,2,3]

Output: 6
Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.

Example 2:

 

Input: root = [-15,10,20,null,null,15,5,-5]

Output: 40

Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = [root.val]  # list because if not it wont be mutable

        def dfs(root):
            currmax = 0
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, currmax)
            rightMax = max(rightMax, currmax)
            maximum[0] = max(maximum[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return maximum


# Helper function to insert nodes in level-order to create the binary tree
def insert_level_order(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root


# Helper function to build a tree from a list
def build_tree(arr):
    if not arr:
        return None
    return insert_level_order(arr, None, 0, len(arr))


# Example usage
if __name__ == "__main__":
    # Example 1
    arr1 = [1, 2, 3]
    root1 = build_tree(arr1)
    solution = Solution()
    print("Maximum Path Sum (Example 1):", solution.maxPathSum(root1))

    # Example 2
    arr2 = [-15, 10, 20, None, None, 15, 5, -5]
    root2 = build_tree(arr2)
    print("Maximum Path Sum (Example 2):", solution.maxPathSum(root2))

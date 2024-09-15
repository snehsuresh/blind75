"""
Depth of Binary Tree
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Input: root = [1,2,3,null,null,4]

Output: 3
"""

from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Solution 1: Recursive dfs
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        res = 1 + max(left_depth, right_depth)

        return res

        # Solution 2: Iterative dfs (preorder) using stack
        # if not root:
        #     return 0
        # stack = [[root, 1]]
        # res = 1
        # while stack:
        #     # pop from stack
        #     node, depth = stack.pop()
        #     if node:
        #         res = max(res, depth)
        #         stack.append([node.left, depth + 1])
        #         stack.append([node.right, depth + 1])
        # return res

        # Solution 3: Iterative BFS using queue
        # q = deque()
        # level = 0
        # if root:
        #     q.append(root)
        # while q:
        #     for i in q:
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1

        # return level


# Helper function to insert nodes in level-order to create a binary tree from a list
def create_binary_tree(values):
    if not values:
        return None
    nodes = [None if val is None else TreeNode(val) for val in values]
    children = nodes[::-1]
    root = children.pop()
    for node in nodes:
        if node:
            if children:
                node.left = children.pop()
            if children:
                node.right = children.pop()
    return root


# Helper function to print the binary tree in level-order
def print_binary_tree(root):
    if not root:
        print([])
        return
    result, level = [], [root]
    while level:
        current_vals = []
        next_level = []
        for node in level:
            if node:
                current_vals.append(node.val)
                next_level.append(node.left)
                next_level.append(node.right)
            else:
                current_vals.append(None)
        if any(v is not None for v in current_vals):  # Avoid printing trailing Nones
            result.extend(current_vals)
        level = next_level
    print(result)


# Example usage
if __name__ == "__main__":
    # Example 1: Binary tree with some nodes
    input_values1 = [1, 2, 3, None, None, 4]
    root1 = create_binary_tree(input_values1)

    print("Original binary tree (Example 1):")
    print_binary_tree(root1)

    # Find the depth of the binary tree using the Solution class
    solution = Solution()
    depth1 = solution.maxDepth(root1)

    # Print the depth
    print(f"Depth of the binary tree (Example 1): {depth1}")

    # Example 2: Empty binary tree
    input_values2 = []
    root2 = create_binary_tree(input_values2)

    print("\nOriginal binary tree (Example 2 - empty):")
    print_binary_tree(root2)

    depth2 = solution.maxDepth(root2)

    print(f"Depth of the binary tree (Example 2 - empty): {depth2}")

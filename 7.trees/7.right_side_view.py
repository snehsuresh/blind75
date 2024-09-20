"""
Binary Tree Right Side View
You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.


Input: root = [1,2,3]

Output: [1,3]
Example 2:

Input: root = [1,2,3,4,5,6,7]

Output: [1,3,7]
"""

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative BFS
        q = deque()
        res = []
        if root:
            q.append(root)
        val = []
        while q:
            val = []
            for i in range(len(q)):
                node = q.popleft()
                val.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val[-1].val)
        return res


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
    # Example 1
    input_values_root1 = [1, 2, 3]

    root1 = create_binary_tree(input_values_root1)

    print("Binary tree root (Example 1):")
    print_binary_tree(root1)

    # Check the right side view using the Solution class
    solution = Solution()
    result1 = solution.rightSideView(root1)

    # Print the result
    print(f"Right side view (Example 1): {result1}")

    # Example 2
    input_values_root2 = [1, 2, 3, 4, 5, 6, 7]

    root2 = create_binary_tree(input_values_root2)

    print("\nBinary tree root (Example 2):")
    print_binary_tree(root2)

    result2 = solution.rightSideView(root2)

    print(f"Right side view (Example 2): {result2}")

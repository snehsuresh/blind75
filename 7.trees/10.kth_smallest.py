"""
Kth Smallest Integer in BST
Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the 
node's key.
The right subtree of every node contains only nodes with keys greater than 
the node's key.
Both the left and right subtrees are also binary search trees.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # First step is that you want to go as left deep as possible using a stack
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


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
    input_values_root1 = [2, 1, 3]
    k1 = 1

    root1 = create_binary_tree(input_values_root1)

    print("Binary tree root (Example 1):")
    print_binary_tree(root1)

    # Find the kth smallest using the Solution class
    solution = Solution()
    result1 = solution.kthSmallest(root1, k1)

    # Print the result
    print(f"Kth smallest element (k={k1}) in Example 1: {result1}")

    # Example 2
    input_values_root2 = [4, 3, 5, 2, None]
    k2 = 4

    root2 = create_binary_tree(input_values_root2)

    print("\nBinary tree root (Example 2):")
    print_binary_tree(root2)

    result2 = solution.kthSmallest(root2, k2)

    print(f"Kth smallest element (k={k2}) in Example 2: {result2}")

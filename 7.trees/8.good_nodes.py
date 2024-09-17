"""
Count Good Nodes in Binary Tree
Within a binary tree, a node x is considered good 
if the path from the root of the tree to the node x 
contains no nodes with a value greater than the value of node x

Given the root of a binary tree root, return the number of good nodes within the tree.

Example 1:



Input: root = [2,1,1,3,null,1,5]

Output: 3


Example 2:

Input: root = [1,2,-1,3,4]

Output: 4
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        print(self.dfs(root, root.val))

    def dfs(self, node, max_val):
        if not node:
            return 0

        if node.val >= max_val:
            res = 1
            max_val = node.val
        else:
            res = 0

        res += self.dfs(node.left, max_val)
        res += self.dfs(node.right, max_val)
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
    input_values_root1 = [2, 1, 1, 3, None, 1, 5]

    root1 = create_binary_tree(input_values_root1)

    print("Binary tree root (Example 1):")
    print_binary_tree(root1)

    # Check the good nodes using the Solution class
    solution = Solution()
    result1 = solution.goodNodes(root1)

    # Print the result
    print(f"Number of good nodes (Example 1): {result1}")

    # Example 2
    input_values_root2 = [1, 2, -1, 3, 4]

    root2 = create_binary_tree(input_values_root2)

    print("\nBinary tree root (Example 2):")
    print_binary_tree(root2)

    result2 = solution.goodNodes(root2)

    print(f"Number of good nodes (Example 2): {result2}")

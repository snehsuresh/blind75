"""
Now this
Valid Binary Search Tree
Given the root of a binary tree, return true if it is a valid binary search tree, 
otherwise return false.

A valid binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
Example 1:



Input: root = [2,1,3]

Output: true
Example 2:



Input: root = [1,2,3]

Output: false
Explanation: The root node's value is 1 but its left child's value is 2 which is greater than 1.


"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lowest, highest):
            if not node:
                return
            if not (lowest < node.val < highest):
                return False
            valid_left = dfs(node.left, lowest, node.val)
            valid_right = dfs(node.right, node.val, highest)
            return valid_left and valid_right

        return dfs(root, float("-inf"), float("inf"))


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
    input_values_root1 = [5, 4, 6, None, None, 3, 7]

    root1 = create_binary_tree(input_values_root1)

    print("Binary tree root (Example 1):")
    print_binary_tree(root1)

    # Check if it is a valid BST using the Solution class
    solution = Solution()
    result1 = solution.isValidBST(root1)

    # Print the result
    print(f"Is valid BST (Example 1): {result1}")

    # Example 2
    input_values_root2 = [1, 2, 3]

    root2 = create_binary_tree(input_values_root2)

    print("\nBinary tree root (Example 2):")
    print_binary_tree(root2)

    result2 = solution.isValidBST(root2)

    print(f"Is valid BST (Example 2): {result2}")

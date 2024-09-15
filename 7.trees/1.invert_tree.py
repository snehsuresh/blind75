"""

Invert a Binary Tree
You are given the root of a binary tree root. Invert the binary tree and return its root.

Input: root = [1,2,3,4,5,6,7]

Output: [1,3,2,7,6,5,4]

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        # swap
        tmp = root.left
        root.left = root.right
        root.right = tmp
        print_binary_tree(root)

        # recursively call
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


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
    # Example 1: Invert a binary tree
    input_values1 = [1, 2, 3, 4, 5, 6, 7]
    root1 = create_binary_tree(input_values1)

    print("Original binary tree (Example 1):")
    print_binary_tree(root1)

    # Invert the binary tree using the Solution class
    solution = Solution()
    inverted_root1 = solution.invertTree(root1)

    # Print the inverted binary tree
    print("Inverted binary tree (Example 1):")
    print_binary_tree(inverted_root1)

    # Example 2: Empty tree
    input_values2 = []
    root2 = create_binary_tree(input_values2)

    print("\nOriginal binary tree (Example 2 - empty):")
    print_binary_tree(root2)

    inverted_root2 = solution.invertTree(root2)

    print("Inverted binary tree (Example 2 - empty):")
    print_binary_tree(inverted_root2)

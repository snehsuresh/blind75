"""
Given the roots of two binary trees p and q, 
return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent 
if they share the exact same structure and the nodes have the same values.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Write your solution here
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
        else:
            return False
        return left and right


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
    # Example 1: Same binary trees
    input_values_p1 = [1, 2, 3]
    input_values_q1 = [1, 2, 3]
    p1 = create_binary_tree(input_values_p1)
    q1 = create_binary_tree(input_values_q1)

    print("Binary tree p (Example 1):")
    print_binary_tree(p1)

    print("Binary tree q (Example 1):")
    print_binary_tree(q1)

    # Check if the binary trees are the same using the Solution class
    solution = Solution()
    result1 = solution.isSameTree(p1, q1)

    # Print the result
    print(f"Are the binary trees the same? (Example 1): {result1}")

    # Example 2: Different structure
    input_values_p2 = [4, 7]
    input_values_q2 = [4, None, 7]
    p2 = create_binary_tree(input_values_p2)
    q2 = create_binary_tree(input_values_q2)

    print("\nBinary tree p (Example 2):")
    print_binary_tree(p2)

    print("Binary tree q (Example 2):")
    print_binary_tree(q2)

    result2 = solution.isSameTree(p2, q2)

    print(f"Are the binary trees the same? (Example 2): {result2}")

    # Example 3: Same structure but different values
    input_values_p3 = [1, 2, 3]
    input_values_q3 = [1, 3, 2]
    p3 = create_binary_tree(input_values_p3)
    q3 = create_binary_tree(input_values_q3)

    print("\nBinary tree p (Example 3):")
    print_binary_tree(p3)

    print("Binary tree q (Example 3):")
    print_binary_tree(q3)

    result3 = solution.isSameTree(p3, q3)

    print(f"Are the binary trees the same? (Example 3): {result3}")

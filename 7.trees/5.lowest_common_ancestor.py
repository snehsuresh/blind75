"""
Lowest Common Ancestor in Binary Search Tree
Given a binary search tree (BST) where all node values are unique, 
and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T 
such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        while True:
            if p.val < root.val and q.val > root.val:
                return root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:  # where the split occurs
                # if root.val == p.val or root.val ==  q.val:
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


# Helper function to find a node by value
def find_node(root: TreeNode, val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    left_search = find_node(root.left, val)
    if left_search:
        return left_search
    return find_node(root.right, val)


# Example usage
if __name__ == "__main__":
    # Example 1
    input_values_root1 = [5, 3, 8, 1, 4, 7, 9, None, 2]
    p1_val, q1_val = 3, 8

    root1 = create_binary_tree(input_values_root1)
    p1 = find_node(root1, p1_val)
    q1 = find_node(root1, q1_val)

    print("Binary tree root (Example 1):")
    print_binary_tree(root1)

    # Check the LCA using the Solution class
    solution = Solution()
    # result1 = solution.lowestCommonAncestor(root1, p1, q1)

    # Print the result
    # print(
    #     f"Lowest Common Ancestor of {p1_val} and {q1_val} (Example 1): {result1.val if result1 else None}"
    # )

    # Example 2
    input_values_root2 = [5, 3, 8, 1, 4, 7, 9, None, 2]
    p2_val, q2_val = 3, 4

    root2 = create_binary_tree(input_values_root2)
    p2 = find_node(root2, p2_val)
    q2 = find_node(root2, q2_val)

    print("\nBinary tree root (Example 2):")
    print_binary_tree(root2)

    result2 = solution.lowestCommonAncestor(root2, p2, q2)

    print(
        f"Lowest Common Ancestor of {p2_val} and {q2_val} (Example 2): {result2.val if result2 else None}"
    )

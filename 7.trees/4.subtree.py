"""
Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the same structure 
and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree 
and all of this node's descendants. The tree tree could also be considered 
as a subtree of itself.

Input: root = [1,2,3,4,5], subRoot = [2,4,5]

Output: true

Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]

Output: false
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            left = self.sameTree(p.left, q.left)
            right = self.sameTree(p.right, q.right)
            return left and right
        else:
            return False


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
    # Example 1: root has a subtree that matches subRoot
    input_values_root1 = [1, 2, 3, 4, 5]
    input_values_subRoot1 = [2, 4, 5]
    root1 = create_binary_tree(input_values_root1)
    subRoot1 = create_binary_tree(input_values_subRoot1)

    print("Binary tree root (Example 1):")
    print_binary_tree(root1)

    print("Subtree subRoot (Example 1):")
    print_binary_tree(subRoot1)

    # Check if subRoot is a subtree of root using the Solution class
    solution = Solution()
    result1 = solution.isSubtree(root1, subRoot1)

    # Print the result
    print(f"Is subRoot a subtree of root? (Example 1): {result1}")

    # Example 2: root does not have a subtree that matches subRoot
    input_values_root2 = [1, 2, 3, 4, 5, None, None, 6]
    input_values_subRoot2 = [2, 4, 5]
    root2 = create_binary_tree(input_values_root2)
    subRoot2 = create_binary_tree(input_values_subRoot2)

    print("\nBinary tree root (Example 2):")
    print_binary_tree(root2)

    print("Subtree subRoot (Example 2):")
    print_binary_tree(subRoot2)

    result2 = solution.isSubtree(root2, subRoot2)

    print(f"Is subRoot a subtree of root? (Example 2): {result2}")

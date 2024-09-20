"""
You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
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
    preorder1 = [1, 2, 4, 5, 7, 3, 6, 8]
    inorder1 = [4, 2, 7, 5, 1, 8, 6, 3]

    solution = Solution()
    root1 = solution.buildTree(preorder1, inorder1)

    print("Binary tree (Example 1):")
    print_binary_tree(root1)

    # Example 2
    preorder2 = [1]
    inorder2 = [1]

    root2 = solution.buildTree(preorder2, inorder2)

    print("\nBinary tree (Example 2):")
    print_binary_tree(root2)

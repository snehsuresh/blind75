"""
Serialize and Deserialize Binary Tree
Solved 
Implement an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting an in-memory structure into 
a sequence of bits so that it can be stored or sent across a network to be 
reconstructed later in another computer environment.

You just need to ensure that a binary tree can be serialized to a string 
and this string can be deserialized to the original tree structure. 
There is no additional restriction on how your serialization/deserialization algorithm should work.

Note: The input/output format in the examples is the same as how NeetCode serializes a binary tree. 
You do not necessarily need to follow this format.

Example 1:



Input: root = [1,2,3,null,null,4,5]

Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []

Output: []
Constraints:

"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0  # pointer

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Example usage
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(5)

    codec = Codec()
    serialized_tree1 = codec.serialize(root1)
    print("Serialized Tree 1:", serialized_tree1)

    deserialized_tree1 = codec.deserialize(serialized_tree1)
    print(
        "Deserialized Tree 1:", codec.serialize(deserialized_tree1)
    )  # Should match serialized_tree1

    # Example 2
    root2 = None
    serialized_tree2 = codec.serialize(root2)
    print("Serialized Tree 2:", serialized_tree2)

    deserialized_tree2 = codec.deserialize(serialized_tree2)
    print(
        "Deserialized Tree 2:", codec.serialize(deserialized_tree2)
    )  # Should match serialized_tree2

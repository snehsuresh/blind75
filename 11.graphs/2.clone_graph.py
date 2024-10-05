"""
Clone Graph
Solved 
Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.

Example 1:



Input: adjList = [[2],[1,3],[2]]

Output: [[2],[1,3],[2]]
Explanation: There are 3 nodes in the graph.
Node 1: val = 1 and neighbors = [2].
Node 2: val = 2 and neighbors = [1, 3].
Node 3: val = 3 and neighbors = [2].

Example 2:



Input: adjList = [[]]

Output: [[]]
Explanation: The graph has one node with no neighbors.

Example 3:

Input: adjList = []

Output: []
Explanation: The graph is empty.


"""

from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None


# Example usage
if __name__ == "__main__":
    # Example 1
    # You will need to create the graph nodes manually to test the solution
    solution = Solution()

    # Test case 1
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    # Setup neighbors
    node1.neighbors = [node2]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2]

    print(
        solution.cloneGraph(node1)
    )  # Expected output is a deep copy of the graph with nodes [1,2,3]

    # Test case 2
    node_single = Node(1)
    print(
        solution.cloneGraph(node_single)
    )  # Expected output is a deep copy of a single node graph

    # Test case 3
    print(solution.cloneGraph(None))  # Expected output: None for an empty graph

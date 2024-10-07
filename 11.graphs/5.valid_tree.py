"""
Valid Tree
Given n nodes labeled from 0 to n - 1 and a list of 
undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.

Example 1:

Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true
Example 2:

Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

Output:
false


Note:
You can assume that no duplicate edges will appear in edges. 
Since all edges are undirected, [0, 1] is the same as [1, 0] and 
thus will not appear together in edges.



What makes a tree valid?

1. No loop
2. All nodes need to be connected

"""

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        # keep track of previous node so that we dont visit it again and accidentally call it a loop
        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False

            return True

        return dfs(0, -1) and n == len(visit)


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    n1 = 5
    edges1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(solution.validTree(n1, edges1))  # Expected output: True

    # Test case 2
    n2 = 5
    edges2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(solution.validTree(n2, edges2))  # Expected output: False

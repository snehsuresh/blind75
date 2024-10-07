"""
Count Connected Components in a graph
There is an undirected graph with n nodes. 
There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1
Example 2:

Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

Output:
2

"""

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]  # each component a parent of itself initially

        # You connect the bigger rank componet with smaller ones (an optimazation, watch video)
        rank = [1] * n  # each have parent 1

        # find parent of a node
        def findParent(n):
            res = n
            while res != par[res]:

                par[res] = par[
                    par[res]
                ]  # not compulsory, but optimization by path compression

                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = findParent(n1), findParent(n2)
            if p1 == p2:
                return 0  # same parent, no need to unionize

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            if union(n1, n2) == 1:
                res -= 1
        return res


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    n1 = 3
    edges1 = [[0, 1], [0, 2]]
    print(solution.countComponents(n1, edges1))  # Expected output: 1

    # Test case 2
    n2 = 6
    edges2 = [[0, 1], [1, 2], [2, 3], [4, 5]]
    print(solution.countComponents(n2, edges2))  # Expected output: 2

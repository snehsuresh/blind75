"""

Count Connected Components
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
        pass


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

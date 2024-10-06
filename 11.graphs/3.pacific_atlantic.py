"""
Course Schedule
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.

Example 1:

Input: numCourses = 2, prerequisites = [[0,1]]

Output: true
Explanation: First take course 1 (no prerequisites) and then take course 0.

Example 2:

Input: numCourses = 2, prerequisites = [[0,1],[1,0]]

Output: false
Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1. So it is impossible.
"""

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or (r, c) in visit
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    heights1 = [[4, 2, 7, 3, 4], [7, 4, 6, 4, 7], [6, 3, 5, 3, 6]]
    print(
        solution.pacificAtlantic(heights1)
    )  # Expected output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

    # Test case 2
    heights2 = [[1], [1]]
    print(solution.pacificAtlantic(heights2))  # Expected output: [[0,0], [1,0]]

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

"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        hMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            hMap[crs].append(pre)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if hMap[crs] == []:
                return True

            visit.add(crs)
            for pre in hMap[crs]:
                canBeFinished = dfs(pre)
                if not canBeFinished:
                    return False

            # We visited a course and finished it, remove it from visit
            visit.remove(crs)
            # remove prereqs since we finished the course, so we finished the prereqs too
            hMap[crs] = []
            return True

        # call dfs for all course
        for c in range(numCourses):
            canBeFinished = dfs(c)
            if not canBeFinished:
                return False

        return True


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    numCourses1 = 2
    prerequisites1 = [[0, 1]]
    print(solution.canFinish(numCourses1, prerequisites1))  # Expected output: True

    # Test case 2
    numCourses2 = 2
    prerequisites2 = [[0, 1], [1, 0]]
    print(solution.canFinish(numCourses2, prerequisites2))  # Expected output: False

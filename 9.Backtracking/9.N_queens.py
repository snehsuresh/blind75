"""
N-Queens
Solved 
The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.

A queen in a chessboard can attack horizontally, vertically, and diagonally.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a unique board layout where the queen pieces are placed. 'Q' indicates a queen and '.' indicates an empty space.

You may return the answer in any order.
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    n1 = 4
    output1 = solution.solveNQueens(n1)
    print("N-Queens solution for n = 4:", output1)

    # Example 2
    n2 = 1
    output2 = solution.solveNQueens(n2)
    print("N-Queens solution for n = 1:", output2)

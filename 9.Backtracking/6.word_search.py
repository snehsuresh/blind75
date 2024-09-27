from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r,c) in path or word[i] != board[r][c] or r<0 or c<0 or r>= rows or c>= cols:
                return False
            
            path.add((r,c))
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            path.remove((r,c))
            return res

        
        for r in rows:
            for c in cols:
                if dfs(r,c,0): return True
        
        return False

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    board1 = [
      ["A", "B", "C", "D"],
      ["S", "A", "A", "T"],
      ["A", "C", "A", "E"]
    ]
    word1 = "CAT"
    output1 = solution.exist(board1, word1)
    print("Is the word 'CAT' present in the grid?:", output1)

    # Example 2
    board2 = [
      ["A", "B", "C", "D"],
      ["S", "A", "A", "T"],
      ["A", "C", "A", "E"]
    ]
    word2 = "BAT"
    output2 = solution.exist(board2, word2)
    print("Is the word 'BAT' present in the grid?:", output2)

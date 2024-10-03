"""
Search for Word II
Given a 2-D grid of characters board and a list of strings words, return all words that 
are present in the grid.

For a word to be present it must be possible to form the word with a path in the 
board with horizontally or vertically neighboring cells. The same cell may not be used 
more than once in a word.

Example 1:

Input:
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
],
words = ["bat","cat","back","backend","stack"]

Output: ["cat","back","backend"]
Example 2:

Input:
board = [
  ["x","o"],
  ["x","o"]
],
words = ["xoxo"]

Output: []
"""

from typing import List


# If you find the pruning with refs optimization difficult, ignore it, code still works
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    board1 = [
        ["a", "b", "c", "d"],
        ["s", "a", "a", "t"],
        ["a", "c", "k", "e"],
        ["a", "c", "d", "n"],
    ]
    words1 = ["bat", "cat", "back", "backend", "stack"]
    print(solution.findWords(board1, words1))  # Output: ["cat", "back", "backend"]

    # Example 2
    board2 = [["x", "o"], ["x", "o"]]
    words2 = ["xoxo"]
    print(solution.findWords(board2, words2))  # Output: []

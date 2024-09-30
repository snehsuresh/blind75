"""
Palindrome Partitioning
Given a string s, split s into substrings where every substring is a palindrome. 
Return all possible lists of palindromic substrings.

You may return the solution in any order.

Example 1:

Input: s = "aab"

Output: [["a","a","b"],["aa","b"]]
Example 2:
 
Input: s = "a"

Output: [["a"]]
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True


"""


If the for loop confuses you, think of it this way. 
In this problem, we are looking for all possible substrings that are palindromes, 
starting from each index of the string. At each step, you need to try all
 substrings from the current index to every possible endpoint in the string. 
 This requires a for loop to explore each potential substring starting at the current position.

 Whereas in, for example combination sum problems, You are explicitly iterating over 
 each number in the list, either including it or skipping it, using two recursive calls

Callstack aab => 0,1,2
dfs(0)
dfs(1)
dfs(2)
dfs(3)
Backtrack to dfs(2)
Backtrack to dfs(1)
dfs(2)
dfs(3)
Backtrack to dfs(2)
Backtrack to dfs(0)
"""


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s1 = "aabb"
    output1 = solution.partition(s1)
    print("Palindrome partitions for 'aab':", output1)

    # Example 2
    s2 = "a"
    output2 = solution.partition(s2)
    print("Palindrome partitions for 'a':", output2)

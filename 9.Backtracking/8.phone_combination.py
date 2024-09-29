"""
Combinations of a Phone Number
You are given a string digits made up of digits from 2 through 9 inclusive.

Each digit (not including 1) is mapped to a set of characters as shown below:

A digit could represent any one of the characters it maps to.

Return all possible letter combinations that digits could represent. 
You may return the answer in any order.
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):

            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    digits1 = "23"
    output1 = solution.letterCombinations(digits1)
    print("Combinations for digits '34':", output1)

    # Example 2
    digits2 = ""
    output2 = solution.letterCombinations(digits2)
    print("Combinations for digits '':", output2)

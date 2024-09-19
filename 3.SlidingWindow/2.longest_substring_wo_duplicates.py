"""
Longest Substring Without Duplicates

Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
"""

s = "zxyzxyz"


# Hint: Sliding window. Maintain a set, remove from set when duplicate


charSet = set()
l = 0
res = 0
for r in range(len(s)):
    while s[r] in charSet:
        charSet.remove(s[l])
        l += 1
    charSet.add(s[r])
    window = r - l + 1
    res = max(res, window)
print(res)

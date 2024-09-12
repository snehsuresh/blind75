"""
Given two strings s and t, return the shortest substring of s such that every character in t, 
including duplicates, is present in the substring. 
If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
"""

# "ADOBECODEBANC"

s = "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"

# Hint: Have = Need

freqMapT = {}
for i in t:
    freqMapT[i] = freqMapT.get(i, 0) + 1

freqMapS = {}
l = 0
have = 0
need = len(freqMapT)
max_window = ""
for r, i in enumerate(s):
    freqMapS[i] = freqMapS.get(i, 0) + 1
    if freqMapS[i] == freqMapT[i]:
        have += 1
    while have == need:
        window = s[l : r + 1]
        if len(window) < len(max_window) or max_window == "":
            max_window = window
        if s[l] in freqMapS:
            freqMapS[s[l]] -= 1
            if freqMapS[s[l]] < freqMapT[s[l]]:
                have -= 1
            if freqMapS[s[l]] == 0:
                freqMapS.pop(s[l], None)
        l += 1

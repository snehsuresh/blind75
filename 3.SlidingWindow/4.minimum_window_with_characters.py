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

freqMapT = {}
for i in range(len(t)):
    freqMapT[t[i]] = freqMapT.get(t[i], 0) + 1

need = len(freqMapT)
have = 0
l = 0
res = []
# freqMapS = {s[l]:1}
freqMapS = {}
max_window = ""
# least_window =
for r in range(len(s)):
    if s[r] in freqMapT:
        freqMapS[s[r]] = freqMapS.get(s[r], 0) + 1
        if freqMapS[s[r]] == freqMapT[s[r]]:
            have += 1
    # validity check
    while have == need:
        curr_window = s[l : r + 1]
        if len(curr_window) < len(max_window) or len(max_window) == 0:
            max_window = curr_window
        if s[l] in freqMapS:
            freqMapS[s[l]] -= 1
            if freqMapS[s[l]] < freqMapT[s[l]]:
                have -= 1
            if freqMapS[s[l]] == 0:
                freqMapS.pop(s[l], None)

        l += 1


print(max_window)

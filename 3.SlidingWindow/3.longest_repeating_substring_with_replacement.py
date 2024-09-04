"""
Longest Repeating Substring With Replacement
You are given a string s consisting of only uppercase english characters and an integer k. 
You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, 
return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
"""

# Hashmap of count.

s = "AABABBA"

k = 1
hMap = {}
l = 0
maximum = 0
res = 0
for r in range(len(s)):
    hMap[s[r]] = hMap.get(s[r], 0) + 1
    maximum = max(maximum, hMap[s[r]])
    window = r - l + 1
    if window - maximum <= k:
        res = max(window, res)
    else:
        l += 1
        hMap[s[l]] -= 1

print(res)

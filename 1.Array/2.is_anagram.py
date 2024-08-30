"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.

Input: s = "racecar", t = "carrace"

Output: true
"""

s = "jar"
t = "jam"

# if len(s) != len(t): return False
sMap = {}
tMap = {}
for i in s:
    sMap[i] = sMap.get(i, 0) + 1
print(sMap)
for i in t:
    tMap[i] = tMap.get(i, 0) + 1
print(tMap)
print(sMap == tMap)

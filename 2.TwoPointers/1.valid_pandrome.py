"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. 
It is also case-insensitive and ignores all non-alphanumeric characters.

Input: s = "Was it a car or a cat I saw?"

Output: true
"""

s = ".,"

start = 0
end = len(s) - 1


def isalnum(c):
    if (
        ord("A") <= ord(c) <= ord("Z")
        or ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9")
    ):
        return True


while start < end:
    while start < end and not isalnum(s[start]):
        start += 1
    while start < end and not isalnum(s[end]):
        end -= 1
    if s[start].lower() != s[end].lower():
        print(False)
    # if s[start].lower() == s[end].lower():
    start += 1
    end -= 1

print(True)

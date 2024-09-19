"""
Validate Parentheses
You are given a string s consisting of the following characters: 
'(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

s = "([{}])"
Output: true

"""

# s = "]"
s = "([{}])"


from collections import deque

stack = deque()
hmap = {
    ")": "(",
    "]": "[",
    "}": "{",
}
for c in s:
    if c not in hmap:
        stack.append(c)
        continue
    if len(stack) == 0 or stack[-1] != hmap[c]:
        print(False)
    stack.pop()

print(stack)

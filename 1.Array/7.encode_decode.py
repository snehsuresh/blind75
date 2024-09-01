"""
Design an algorithm to encode a list of strings to a single string. 
The encoded string is then decoded back to the original list of strings.
Please implement encode and decode

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
"""

a = ["neet", "code", "love", "you"]


# def encode(strs):
#     res = ""
#     for str in strs:
#         res = res + ";" + str
#     return res


# def decode(s):
#     res = []
#     word = ""
#     for char in s:
#         if char == ";":
#             if len(word) > 0:
#                 res.append(word)
#             word = ""
#         else:
#             word += char
#     if len(word) > 0:
#         res.append(word)
#     return res


def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res


def decode(s):
    res = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j

    return res


encoded = encode(a)
decoded = decode(encoded)

"""
Anagram Groups

Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

"""

# -----------Hash map method------------ More efficient, tricky

from collections import defaultdict


def group_anagrams(strs):
    anagram_map = defaultdict(list)

    for s in strs:
        char_count = [0] * 26

        for char in s:
            char_count[ord(char) - ord("a")] += 1
        anagram_map[tuple(char_count)].append(s)
    return anagram_map.values()


strs = ["act", "pots", "tops", "cat", "stop", "hat"]

print(group_anagrams(strs))


# ----------sort method ------------- Less efficient, easy


# def group_anagrams_sort(strs):
#     # anagram_map = {}
#     anagram_map = defaultdict(list)

#     for s in strs:
#         sorted_key = "".join(sorted(s))
#         anagram_map[sorted_key].append(s)

#     print(anagram_map)


# strs = ["act", "pots", "tops", "cat", "stop", "hat"]

# print(group_anagrams_sort(strs))

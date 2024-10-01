"""
Implement Prefix Tree
A prefix tree (also known as a trie) is a tree data structure used to efficiently store 
and retrieve keys in a set of strings. Some applications of this data structure include 
auto-complete and spell checker systems.

Implement the PrefixTree class:

PrefixTree() Initializes the prefix tree object.

insert(String word) Inserts the string word into the prefix tree.

search(String word) Returns true if the string word is in the prefix tree 
(i.e., was inserted before), and false otherwise.

startsWith(String prefix) Returns true if there is a previously inserted string 
word that has the prefix prefix, and false otherwise.
Example 1:

Input: 
["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]

Output:
[null, null, true, false, true, null, true]

Explanation:
PrefixTree prefixTree = new PrefixTree();
prefixTree.insert("dog");
prefixTree.search("dog");    // return true
prefixTree.search("do");     // return false
prefixTree.startsWith("do"); // return true
prefixTree.insert("do");
prefixTree.search("do");     // return true
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


if __name__ == "__main__":
    prefixTree = PrefixTree()

    prefixTree.insert("dog")
    print(prefixTree.search("dog"))  # Output: True
    print(prefixTree.search("do"))  # Output: False
    print(prefixTree.startsWith("do"))  # Output: True
    prefixTree.insert("do")
    print(prefixTree.search("do"))  # Output: True

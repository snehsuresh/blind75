"""
Design Word Search Data Structure
Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

addWord(word) Adds word to the data structure.
search(word) Returns true if there is any string in the 
data structure that matches word or false otherwise. word may contain dots '.' 
where dots can be matched with any letter.

Example 1:

Input:
["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]

Output:
[null, null, null, null, false, true, true, true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true
"""


class TrieNode:
    def __init__(self, value):
        self.children = {}
        self.endOfWord = False
        # only for debugging purpose
        self.value = value


class WordDictionary:

    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word: str) -> None:

        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord

        return dfs(0, self.root)


# Example usage
if __name__ == "__main__":
    wordDictionary = WordDictionary()

    # Example 1
    wordDictionary.addWord("day")
    wordDictionary.addWord("bay")
    wordDictionary.addWord("may")

    print(wordDictionary.search(".ay"))
    print(wordDictionary.search("b.."))
    # Output: True
    # Output: True
    print(wordDictionary.search("say"))  # Output: False
    print(wordDictionary.search("day"))  # Output: True

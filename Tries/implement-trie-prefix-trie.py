from typing import Dict


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.terminal: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.terminal = True

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.terminal  # Prefixes don't count as entries in the Trie

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True


"""
Algorithm:
Each node contains a dictionary mapping a character to another trie node, 
representing its children and a flag determining whether the node is the end of 
a word or not.

Time Complexity:
All operations are O(n) since we have to go through the string exactly once.

"""

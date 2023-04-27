# O(n) time

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            letter_count = [0] * 26
            for char in word:
                letter_count[ord(char) - ord("a")] += 1
            res[tuple(letter_count)].append(word)

        return res.values()

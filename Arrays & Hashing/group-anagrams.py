from typing import List
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


sol = Solution()
print(sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(sol.groupAnagrams(strs=[""]))
print(sol.groupAnagrams(strs=["a"]))

"""
Algorithm:
We create a dictionary of the following format:
{[letter count array]: [list of words]}
We go through each word in strs and then compute the frequency of each letter.
Then we add that word to the associated hashmap entry.

Time Complexity:
We go through strs once giving a time complexity of O(n). We also loop through
each word so we can find that the worst case time complexity is O(mn) where n is
the length of strs and m is the length of the longest word.
"""

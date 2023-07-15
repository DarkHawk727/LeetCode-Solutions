class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


sol = Solution()
print(sol.isAnagram(s="anagram", t="nagaram"))
print(sol.isAnagram(s="rat", t="car"))

"""
Algorithm:
We sort s and t by alphabetical order and check if they are equal. 

Time Complexity:
Sorting takes O(nlog(n)) time which we do twice and the check for equality which
is O(n). This gives us a overall time complexity of O(nlog(n)).
"""

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for c1, c2 in zip(s, s[1:]):
            score += abs(ord(c2) - ord(c1))
        return score


sol = Solution()
print(sol.scoreOfString("code"))  # 13
print(sol.scoreOfString("hello"))  #

"""
Algorithm:
We iterate over consecutive pairs of letters and accumulate the difference in their ASCII representations.

Time Complexity:
Since we only traverse the string once, the time complexity is in O(n) where n is the length of the string.
"""

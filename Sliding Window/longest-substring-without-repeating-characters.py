class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        substring = set()
        longest_so_far = 0

        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
            substring.add(s[right])
            longest_so_far = max(longest_so_far, right - left + 1)

        return longest_so_far


sol = Solution()
print(sol.lengthOfLongestSubstring(s="abcabcbb"))
print(sol.lengthOfLongestSubstring(s="bbbbb"))
print(sol.lengthOfLongestSubstring(s="pwwkew"))

"""
Algorithm:
We initialize a left pointer to 0 and a set. We then loop through the indices of
the string and if the rightmost character is already in the substring, we remove
the leftmost character from the substring, checking for the maximum along the 
way.

Time Complexity:
Since we are only going through the string once, O(n)
"""

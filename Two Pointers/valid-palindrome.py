class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        return s == s[::-1]


"""
Algorithm:
Filter the string bt all alphanumeric characters and make them lower case.
Then check if the string equals itself backward.

Time Complexity:
O(n) since we are going through the string once.
"""

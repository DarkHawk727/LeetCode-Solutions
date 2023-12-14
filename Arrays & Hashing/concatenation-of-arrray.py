from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2


sol = Solution()
print(sol.getConcatenation(nums=[1, 2, 1]))
print(sol.getConcatenation(nums=[1, 3, 2, 1]))


"""
Algorithm:
We take advantage of Python's overloaded multiplication operator for lists.

Time Complexity:
I don't know how Python represents lists internally so I can't say.
"""

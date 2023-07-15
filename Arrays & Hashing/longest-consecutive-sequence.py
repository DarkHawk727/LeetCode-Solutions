from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        frequency_set = set(nums)
        longest, length = 0, 0

        for num in nums:
            if (num - 1) not in frequency_set:
                length = 0
                while (num + length) in frequency_set:
                    length += 1
                longest = max(length, longest)
        return longest


sol = Solution()
print(sol.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
print(sol.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))

"""
Algorithm:
We create a set of nums.
Then we loop through nums. If the number before does not exist, that means that
it is the start of a sequence. Then we check if num+length is also in the set,
incrementing it while it is. Then we update the current longest to be the max of
the old longest sequence and the current one.

Time Complexity:
Since we are only going through nums once, the time complexity is O(n).
Set membership is O(1).
Therefore, the overall time complexity is O(n).
"""

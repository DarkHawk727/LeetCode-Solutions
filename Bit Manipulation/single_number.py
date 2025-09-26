from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for elem in nums:
            ans ^= elem
        return ans


sol = Solution()
print(sol.singleNumber([3, 2, 3]))  # 2
print(sol.singleNumber([7, 6, 6, 7, 8]))  # 8

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        before = 1
        after = 1
        for i in range(len(nums)):
            ans[i] = before
            before *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= after
            after *= nums[i]

        return ans


sol = Solution()
print(sol.productExceptSelf(nums=[1, 2, 3, 4]))
print(sol.productExceptSelf(nums=[-1, 1, 0, -3, 3]))

"""
Algorithm:
We initialize an arrays of 1's of length of nums. We then loop through nums
while computing the product of all the numbers before it and after and then
multiplying the two together.

Time Complexity:
We go through nums twice, giving the overall time complexity O(n).
"""

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

# O(n) time

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in number_map:
                return [i, number_map[complement]]
            number_map[nums[i]] = i

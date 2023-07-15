from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in number_map:
                return [i, number_map[complement]]
            number_map[nums[i]] = i


sol = Solution()
print(sol.twoSum(nums=[2, 7, 11, 15], target=9))
print(sol.twoSum(nums=[3, 2, 4], target=6))
print(sol.twoSum(nums=[3, 3], target=6))

"""
Algorithm:
We define a hashmap called number_map of the following format:
{value: index in nums}.
We go through nums and check if nums[i]-target is in number_map. If it is, we
return the indexes or else we add to number_map.

Time Complexity:
Since we are only going through nums once, the time complexity is O(n). 
Additionally, hashmap lookup is constant. This makes our overall complexity 
O(n).
"""

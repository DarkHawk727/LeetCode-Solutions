from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return ans


sol = Solution()
print(sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
print(sol.threeSum(nums=[0, 1, 1]))
print(sol.threeSum(nums=[0, 0, 0]))


"""
Algorithm:
We sort nums. We then loop over it, skipping the duplicates. We then set a left
and right pointer equal to the next number and the end and then do the same
algorithm as two-sum-2-input-array-is-sorted.

Time Complexity:
Since we have to sort the array: O(nlog(n)). Sincwe we have two nested while 
loops, this adds an O(n^2) to our overall complexity.
Taking the dominant term, our final time complexity is O(n^2).
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1


sol = Solution()
print(sol.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(sol.search(nums=[-1, 0, 3, 5, 9, 12], target=2))


"""
Algorithm:
We start at the middle, if the target is smaller, then we shift the right 
pointer to the middle. Conversely, if the target is bigger, then we shift the 
left pointer to the middle.

Time Complexity:
Since we are halving the list on each iteration, the time complexity is 
O(log_2(n)).
"""

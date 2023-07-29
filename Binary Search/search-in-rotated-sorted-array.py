from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle

            if nums[left] <= nums[middle]:
                if nums[middle] < target or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if nums[middle] > target or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1


sol = Solution()
print(sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
print(sol.search(nums=[1], target=0))


"""
Algorithm:
We initialize a left and right pointer, then while left <= right, we check if 
the number in the middle is the target. If the left number is smaller than the 
middle one, we check if the middle is larger than the target and smaller than 
the left one, if it is, we set the left to the number after the middle, otherwise
right becomes the one before the middle. Otherwise, we check to see if the middle
is smaller than the target or if the targer is smaller than the right number, 
setting the right to the one before the middle or the left to the one after the 
middle accordingly. 

Time Complexity:
Since this is like binary search, the time complexity is O(log_2(n)).
"""

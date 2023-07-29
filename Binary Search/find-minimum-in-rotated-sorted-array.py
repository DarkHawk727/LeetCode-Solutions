from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        return nums[left]


sol = Solution()
print(sol.findMin(nums=[3, 4, 5, 1, 2]))
print(sol.findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
print(sol.findMin(nums=[11, 13, 15, 17]))


"""
Algorithm:
We initialize a left and right pointer. We compute the middle to be half the 
distance between the right and left, and then add left. If the number at the 
middle is greater than the right, we set the left to be the element after the 
middle otherwise, the right is the middle. We return the number on the left.

Time Complexity:
Since we are using a binary search-like algorithm, the time complexity is 
O(log_2(n)).
"""

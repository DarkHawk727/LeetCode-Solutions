from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left


sol = Solution()
test_1 = [1, 1, 2]
print(sol.removeDuplicates(nums=test_1), test_1)
test_2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(sol.removeDuplicates(nums=test_2), test_2)


"""
Algorithm:
We initialize the left pointer to 1. We then loop through the second element 
onwards. If the previous rightmost element is different from the current 
rightmost element, then we set the left element to the new value and increment 
the left pointer.

Time Complexity:
Since we only loop through the array once, O(n)
"""

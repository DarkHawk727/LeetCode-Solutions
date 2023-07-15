from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]


sol = Solution()
print(sol.twoSum(numbers=[2, 7, 11, 15], target=9))
print(sol.twoSum(numbers=[2, 3, 4], target=6))
print(sol.twoSum(numbers=[-1, 0], target=-1))

"""
Algorithm:
We initialize a left and right pointer to be the start and end of numbers. If 
the sum of the numbers at numbers[left] and numbers[right] is greater than the
targer, we decrement the right pointer, and increment left in the other case.

Time Complexity:
Since left and right will start at opposite ends of numbers and work to the 
middle, the overall time complexity is O(n).
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0

        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area


sol = Solution()
print(sol.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(sol.maxArea(height=[1, 1]))

"""
Algorithm:
We initialize a left and right pointer to opposite ends of height. If the height
at the left pointer is less than the height of the right, we move the left 
forward; otherwise we move the right backward. We also keep track of the maximum
area so far.

Time Complexity:
Since we have only a while loop that would stop when left==right where left and 
right have been initialized to opposite ends of the array, our overall time 
complexity is O(n).
"""

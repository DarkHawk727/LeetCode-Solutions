from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


"""
Algorithm:
We go through each element of the array, if it is not equal to the value, we 
swap it with the kth element and increment k.

Time Complexity:
Since we are only going through the array once, O(n) 
"""

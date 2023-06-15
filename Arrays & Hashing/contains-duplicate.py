from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False


"""
Algorithm:
We want to go through each number in nums and add it to a set, if we encounter 
a number that is already in the set, we return true because we have found a 
duplicate. If we reach the end, the numbers contained no duplicates.

Time Complexity:
Since we are only looking through the nums array once, we can say its time
complexity is O(n). Additionally, checking membership in num_set is O(1).
This gives the program an overall runtime of O(n), where n is the length of 
nums.
"""

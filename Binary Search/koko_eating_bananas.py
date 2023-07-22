from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_rate = max(piles)

        while left <= right:
            current_rate = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += ceil(pile / current_rate)

            if hours <= h:
                min_rate = min(min_rate, current_rate)
                right = current_rate + 1
            else:
                left = current_rate + 1

        return min_rate


sol = Solution()

assert sol.minEatingSpeed(piles=[3, 6, 7, 11], h=8) == 4
assert sol.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5) == 30
assert sol.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6) == 23

"""
Algorithm:
We initialize a left and right pointer to be the 1 and the maximum values of 
piles. We then perform binary search on these pointers. On each iteration, we
check if the total numbers hours does not exceed h.

Time Complexity:
Since we are running binary search over a list with max(piles) elements and in
each loop, we are looping over all elements in piles, we get an overall time
complexity of O(log_2(max(piles)*len(piles))) = O(n*log_2(p)).
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            max_profit = max(max_profit, price - lowest)
        return max_profit


sol = Solution()

print(sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(sol.maxProfit(prices=[7, 6, 4, 3, 1]))


"""
Algorithm:
We set the lowest price to be the first element. We then go through prices and
 find the smaller price, and then record the maximum profit.

Time Complexity:
Since we are iterating through the array only once, the overall complexity is
O(n).
"""

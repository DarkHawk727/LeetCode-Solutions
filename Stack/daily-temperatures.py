from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans, stack = [0] * (len(temperatures) + 1), []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                ans[stack_index] = index - stack_index
            stack.append([temp, index])
        return ans


sol = Solution()
print(sol.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
print(sol.dailyTemperatures(temperatures=[30, 40, 50, 60]))
print(sol.dailyTemperatures(temperatures=[30, 60, 90]))

"""
Algorithm:
Go through each element in temperatures. While the stack is not empty and
the current temperature is greater than the bottom, pop the last temperature and
its corresponding index and assign the difference between the current index and 
the popped index (which is the number of days since a warmer temperature) to the
ans list.

Time Complexity:
Since we only go through temperatures once, the time is O(n).
"""

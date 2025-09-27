class Solution:
    def climbStairs(self, n: int, memo: dict = {}) -> int:
        if n in memo:
            return memo[n]
        if n <= 2:
            return n
        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
        return memo[n]


sol = Solution()
print(sol.climbStairs(2))  # 2
print(sol.climbStairs(3))  # 3
print(sol.climbStairs(4))  # 5
print(sol.climbStairs(44))  # 1134903170

"""
Algorithm:
For a given n, we notice that the number of ways to climb to that stairs is the sum of the number of ways to climb where
we end with a single step and the case where we end with a double step. Since the leetcode testcases were larger than
Neetcode, I had to memoize this function.

Time Complexity:
For the naive solution, since for a given recursive call, we produce 2 calls, the overall time complexity is in O(2^n).
The memoized solution stores previous values and the dictionary lookup is consant so we end up with a runtime in O(n).
"""

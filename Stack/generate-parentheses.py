from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        def backtrack(open: int, close: int) -> None:
            if open == close == n:
                ans.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()

        backtrack(0, 0)
        return ans


sol = Solution()
print(sol.generateParenthesis(n=3))
print(sol.generateParenthesis(n=1))

"""
Algorithm:
If open = close = n, then we return.
If close < open, then we append a ), backtrack, and pop it from the stack.

Time Complexity:
O(2^(2n)*n) cause recursion.
"""

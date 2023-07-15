from typing import List
import operator as op


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_map = {
            "+": lambda x, y: x + y,
            "*": lambda x, y: x * y,
            "-": lambda x, y: y - x,
            "/": lambda x, y: int(y / x),
        }
        stack = []
        for token in tokens:
            if token not in operator_map:
                stack.append(int(token))
            else:
                a, b = stack.pop(), stack.pop()
                stack.append(operator_map[token](a, b))
        return stack[0]


sol = Solution()
print(sol.evalRPN(tokens=["2", "1", "+", "3", "*"]))
print(sol.evalRPN(tokens=["4", "13", "5", "/", "+"]))
print(
    sol.evalRPN(
        tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)

"""
Algorithm:
Define a operator map that maps a symbol to a lambda function for the associated
operation.
Go through each element in tokens and if the token is not in the operator map,
add it to the stack. Otherwise, pop two elements from the stack and perform the
associated operation on them, adding the result back to the stack.

Time Complexity:
Since we only go through tokens once, the time complexity is O(n)
"""

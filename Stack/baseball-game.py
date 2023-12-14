from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack: List[int] = []
        for operation in operations:
            # Since .isnumeric() can't handle negative numbers on its own.
            # We could have also modified the order of checking to make this a else.
            if operation.strip("-").isnumeric():
                stack.append(int(operation))
            elif operation == "C":
                stack.pop()
            elif operation == "D":
                stack.append(2 * stack[-1])
            elif operation == "+":
                stack.append(stack[-1] + stack[-2])
        return sum(stack)


sol = Solution()
print(sol.calPoints(operations=["5", "2", "C", "D", "+"]))
print(sol.calPoints(operations=["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(sol.calPoints(operations=["1", "C"]))


"""
Algorithm:
We go through each operation, if its a numeric type (being sure to process for 
negative numbers), we append it to the stack. If it's "C", then we pop from the
stack. If it's a "D", we push double the top value. If it's a "+" we add the 
top 2 values and push that to the stack. We return a sum of all the elements in 
the stack.

Time Complexity:
Each operation on the stack is O(1) and we go through each operation once, O(n).
"""

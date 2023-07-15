class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for bracket in s:
            if bracket not in Map:
                stack.append(bracket)
                continue
            if not stack or stack[-1] != Map[bracket]:
                return False
            stack.pop()

        return not stack


sol = Solution()
print(sol.isValid(s="()"))
print(sol.isValid(s="()[]{}"))
print(sol.isValid(s="(]"))

"""
Algorithm:
We go through each element in s, if said element is not in the map, we append it
to the stack. If the stack is empty or the last element is not the associated
open bracket, then we return false. Otherwise, we pop the element.

Time Complexity:
Since we are only looping through s once, the time complexity is O(n). All other
operations are O(1).
"""

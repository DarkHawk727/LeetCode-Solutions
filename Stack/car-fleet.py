from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), reverse=True)  # Sorted by position.
        stack = []

        for p, s in cars:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


"""
Algorithm:
First we construct a list of tuples for the cars of the form 
(speed[i], position[i]). We then sort in in decreasing order by position. We
then loop through all the cars and compute how long it would take for them to 
reach the finish line and add it to the stack. If the length of the stack is 
greater than 2 and the most recent element is less than the previous element,
we pop it from the stack. Finally, we return the length of the stack.

Time Complexity:
Sorting the cars take O(nlog(n)) and going through the cars is O(n).
"""

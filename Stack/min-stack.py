class MinStack:
    def __init__(self):
        self.stack = []
        self.minsofar = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minsofar.append(min(val, self.minsofar[-1] if self.minsofar else val))

    def pop(self) -> None:
        self.stack.pop()
        self.minsofar.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minsofar[-1]


"""
Algorithm:
We create a regular stack with its associated operations. The addition is of
another stack which keeps track of the minimum so far, which we also update
accordingly.

Time Complexity:
pop(), top(), and getmin() are all array lookups so O(1).
push() is amortized O(1).
"""

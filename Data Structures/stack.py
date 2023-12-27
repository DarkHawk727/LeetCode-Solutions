from typing import Any, List


class Stack:
    def __init__(self) -> None:
        self.vals: List[Any] = []

    def push(self, item: Any) -> None:
        self.vals.append(item)

    def pop(self) -> Any:
        return self.vals.pop()

    def peek(self) -> Any:
        return self.vals[-1]

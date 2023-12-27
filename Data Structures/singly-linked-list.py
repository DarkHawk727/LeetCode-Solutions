from __future__ import annotations

from typing import Any, List, Optional


class ListNode:
    def __init__(self, val: Any = None, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> Any:
        current: Optional[ListNode] = self.head.next
        i: int = 0
        while current:
            if i == index:
                return current.val
            i += 1
            current = current.next
        return -1

    def insertHead(self, val: Any) -> None:
        new_node: ListNode = ListNode(val=val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: Any) -> None:
        self.tail.next = ListNode(val=val)
        self.tail = self.tail.next

    def insertIndex(self, index: int, val: Any) -> None:
        new_node: ListNode = ListNode(val=val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current: Optional[ListNode] = self.head
        i: int = 0

        while current and i < index - 1:
            i += 1
            current = current.next

        if current:
            new_node.next = current.next
            current.next = new_node

    def remove(self, index: int) -> bool:
        current: Optional[ListNode] = self.head
        i: int = 0
        while i < index and current:
            i += 1
            current = current.next

        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return True
        return False

    def print(self) -> None:
        current = self.head.next
        while current.next:
            print(current.val, end="->")
            current = current.next
        print(current.val)

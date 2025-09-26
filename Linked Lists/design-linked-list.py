from __future__ import annotations

from typing import List, Optional


class ListNode:
    def __init__(
        self,
        val: int,
        prev: Optional[ListNode] = None,
        next: Optional[ListNode] = None,
    ) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        current: Optional[ListNode] = self.head.next
        i: int = 0
        while current:
            if i == index:
                return current.val
            i += 1
            current = current.next
        return -1

    def addAtHead(self, val: int) -> None:
        new_node, prev, next = ListNode(val=val), self.head, self.head.next
        new_node.next, new_node.prev = next, prev
        next.prev, prev.next = new_node, new_node

    def addAtTail(self, val: int) -> None:
        new_node, prev, next = ListNode(val=val), self.tail.prev, self.tail
        new_node.next, new_node.prev = next, prev
        next.prev, prev.next = new_node, new_node

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.head.next
        while node and index > 0:
            index -= 1
            node = node.next

        if node and index == 0:
            new_node, prev = ListNode(val=val), node.prev
            new_node.next, new_node.prev = node, prev
            node.prev, node.next = new_node, new_node

    def deleteAtIndex(self, index: int) -> None:
        node: Optional[ListNode] = self.head.next
        while node and index > 0:
            index -= 1
            node = node.next

        if node and node != self.tail and index == 0:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev


ll = MyLinkedList()
ll.addAtHead(val=1)
ll.addAtTail(val=3)
ll.addAtIndex(index=1, val=2)
print(ll.get(index=1))
ll.deleteAtIndex(index=1)
print(ll.get(index=1))

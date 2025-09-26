from __future__ import annotations

from typing import Optional


# Helper
def print_ll(head: Optional[ListNode]) -> None:
    if not head:
        print()
    else:
        current = head
        while current.next:
            print(current.val, end=", ")
            current = current.next
        print()


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


sol = Solution()
ll1 = ListNode(
    val=1,
    next=ListNode(
        val=2,
        next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None))),
    ),
)
print_ll(head=sol.reverseList(head=ll1))

ll2 = ListNode(val=1, next=ListNode(val=2, next=None))
print_ll(head=sol.reverseList(head=ll2))

ll3 = None
print_ll(head=sol.reverseList(head=ll3))


"""
Algorithm:
We start be creating a ListNode with the value of the head and which points to
nothing. We then traverse the linked list and "wrap" more ListNodes around the 
original ListNode.

Time Complexity:
Since we are only traversing the LinkedList once, it's O(n).
"""

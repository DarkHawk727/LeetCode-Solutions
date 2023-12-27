from __future__ import annotations
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    # Extra for printing
    def __repr__(self) -> str:
        current = self
        result = ""
        while current.next:
            result += str(current.val) + " -> "
            current = current.next
        result += str(current.val)
        return result


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        placeholder: ListNode = ListNode()
        tail = placeholder

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return placeholder.next


sol = Solution()

print(
    sol.mergeTwoLists(
        list1=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None))),
        list2=ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None))),
    )
)

print(sol.mergeTwoLists(list1=None, list2=None))

print(sol.mergeTwoLists(list1=None, list2=ListNode(val=0, next=None)))


"""
Algorithm:
We iterate through the linked lists, adding the smaller element to our answer.
If either one finishes before the other, we simply append the remaining portion
to the answer.

Time Complexity:
Since we are traversing the linked lists only once, it's O(n).
"""

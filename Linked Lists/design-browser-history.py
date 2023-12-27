from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(
        self, val: str, prev: Optional[ListNode] = None, next: Optional[ListNode] = None
    ) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:
    def __init__(self, homepage: str):
        self.current_tab = ListNode(val=homepage)

    def visit(self, url: str) -> None:
        self.current_tab.next = ListNode(val=url, prev=self.current_tab)
        self.current_tab = self.current_tab.next

    def back(self, steps: int) -> str:
        while self.current_tab.prev and steps > 0:
            self.current_tab = self.current_tab.prev
            steps -= 1

        return self.current_tab.val

    def forward(self, steps: int) -> str:
        while self.current_tab.next and steps > 0:
            self.current_tab = self.current_tab.next
            steps -= 1

        return self.current_tab.val


bh = BrowserHistory(homepage="leetcode.com")
bh.visit(url="google.com")
bh.visit(url="facebook.com")
bh.visit(url="youtube.com")
print(bh.back(steps=1))
print(bh.back(steps=1))
print(bh.forward(steps=1))
bh.visit(url="linkedin.com")
print(bh.forward(steps=2))
print(bh.back(steps=2))
print(bh.back(steps=7))


"""
Algorithm:
We use a doubly lined list for this problem. Visiting just adds a new node after 
the current node, overwriting the previous ones. Going front and back is just 
traversal.

Time Complexity:
visit is O(1) the other two are O(n).
"""

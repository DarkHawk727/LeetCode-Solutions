from typing import Dict, List, Tuple
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.map: Dict[List[Tuple[str, int]]] = defaultdict(lambda: [])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.map.get(key, [])

        left, right = 0, len(values) - 1
        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] <= timestamp:
                res = values[middle][0]
                left = middle + 1
            else:
                right = middle - 1

        return res


tm = TimeMap()
tm.set(key="foo", value="bar", timestamp=1)
print(tm.get(key="foo", timestamp=1))
print(tm.get(key="foo", timestamp=3))
tm.set(key="foo", value="bar2", timestamp=4)
print(tm.get(key="foo", timestamp=4))
print(tm.get(key="foo", timestamp=5))


"""
Algorithm:
Our timemap is a default dictionary of the form:
{
    key: [(value, timestamp)]
}
Initializing and setting elements is fairly straight-forward.
We run binary search for the get method. Setting left and right to be opposite 
ends of the array, and then while left <= right, we check to see if the middle 
element has a less than or equal timestamp, updating the left and right pointers
accordingly

Time Complexity:
Initializing and setting are O(1). Get is binary search so O(log_2(n))
"""

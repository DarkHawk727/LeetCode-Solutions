from typing import List
from itertools import chain


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        collapsed = list(chain.from_iterable(matrix))
        left, right = 0, len(collapsed) - 1
        while left <= right:
            middle = (left + right) // 2
            if collapsed[middle] > target:
                right = middle - 1
            elif collapsed[middle] < target:
                left = middle + 1
            else:
                return True
        return False


sol = Solution()
print(
    sol.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
    )
)
print(
    sol.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13
    )
)

"""
Algorithm:
We first flattern the matrix into a single list and then we perform binary 
search.


Time Complexity:
Since we are halving the list on each iteration, the time complexity is 
O(log_2(m+n)).
"""

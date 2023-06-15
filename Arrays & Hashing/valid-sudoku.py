from typing import List, Tuple
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        subsquares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (
                    board[i][j] in rows[i]
                    or board[i][j] in columns[j]
                    or board[i][j] in subsquares[(i // 3, j // 3)]
                ):
                    return False
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                subsquares[(i // 3, j // 3)].add(board[i][j])

        return True


"""
Algorithm:
We create dictionaries mapping row, column a, subsquare indicies to a set of the
digits. Then we loop through the board and if the current digit is already in
its associated row, column, or subsquare we return false or else we add it to
the associated dictionaries and move on.

Time Complexity:
Since we are looping through the entire board, the complexity is O(n^2). All
other operations are constant (dictionary lookup, addition).
However, since the for loops always go to 9, it is technically O(1).
"""

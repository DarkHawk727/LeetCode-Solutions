from typing import List, Set, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r: int, c: int):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        if not grid:
            return 0
        else:
            islands = 0
            rows, cols = len(grid), len(grid[0])
            visit: Set[Tuple[int, int]] = set()
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == "1" and (r, c) not in visit:
                        islands += 1
                        dfs(r, c)
            print(visit)
            return islands


sol = Solution()
print(
    sol.numIslands(
        [
            ["0", "1", "1", "1", "0"],
            ["0", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)

print(
    sol.numIslands(
        [
            ["1", "1", "0", "0", "1"],
            ["1", "1", "0", "0", "1"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)


"""
Algorithm:


Time Complexity:

"""

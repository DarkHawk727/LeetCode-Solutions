from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        CIRCULAR, SQUARE = 0, 1
        # We can do this since students[i]={0,1}
        n_square = sum(students)  # square=1
        n_circular = len(students) - n_square  # circular=0

        for sandwich in sandwiches:
            if sandwich == SQUARE:
                if n_square == 0:
                    break
                n_square -= 1
            else:
                if n_circular == 0:
                    break
                n_circular -= 1
        return n_square + n_circular


sol = Solution()
print(sol.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))  # 0
print(sol.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))  # 3

"""
Algorithm:
Since students can move, we can simply count the number of students who prefer each type of sandwich. Then we go through
the sandwiches in order and check if 

Time Complexity:
Summing students and computing its length are both in O(n). We then traverse sandwiches in order, which is also in O(n).
This gives us an overall time complexity in O(n).
"""

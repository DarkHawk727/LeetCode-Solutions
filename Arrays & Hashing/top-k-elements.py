from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        frequency_arr = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            counts[num] += 1

        for num, count in counts.items():
            frequency_arr[count].append(num)

        ans = []
        for i in range(len(frequency_arr) - 1, 0, -1):
            ans += frequency_arr[i]
            if len(ans) == k:
                return ans


"""
Algorithm:
We create a dictionary of the format: {number: count}
We create an array of arrays where each element is the list of numbers that
occur the same times as the index.
We first populate the count dictionary and then the frequency array.
Finally, we go backwards through the frequency array, appending all elements
and stop when the length of the answer is k.

Time Complexity:
Creating the frequency array is O(n). Going through the nums array once is O(n).
Going through the items of counts is O(m) where m is the number of distinct 
elements in nums. Going through the frequency array is at most O(n).
This gives us an overall time complexity of O(n+m) where m <= n, so it 
simplifies to O(n).

"""

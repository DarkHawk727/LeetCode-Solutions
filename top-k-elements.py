# O(n) time
from collections import defaultdict

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

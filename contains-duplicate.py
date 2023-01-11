class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time complexity should be O(n) since the length is O(1) but converting from list to set is O(n)
        # This version is slighly optimized since it also checks if the next element is already in the set
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
        

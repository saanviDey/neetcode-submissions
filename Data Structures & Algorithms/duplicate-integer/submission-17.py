class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_seen = {}
        for i, n in enumerate(nums):
            if n in has_seen:
                return True
            has_seen[n] = i
        
        return False
        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_seen = []
        for n in nums:
            if n in nums_seen:
                return True
            nums_seen.append(n)
        return False
        
        
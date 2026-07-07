class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_seen = {}
        # use a hashmap to see if a certain value exists
        # key : value -> index : value
        # if a number is in a hashmap return true
        # else add it to the hashmap
        # return false if we're done with the array and no duplicates
        for i, n in enumerate(nums):
            if n in has_seen:
                return True
            has_seen[n] = i
        
        print(nums)
        print(has_seen)
        return False
        
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        nums.sort()
        print(nums)
        start = nums[0]
        counter = 1
        max_counter = 0

        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            print("current diff: ", diff)
            if diff == 0 or diff == 1:
                if diff == 1:
                    counter = counter + 1
            else:
                start = nums[i + 1]
                counter = 1
            
            if (counter > max_counter):
                    max_counter = counter
        
        return max_counter

        
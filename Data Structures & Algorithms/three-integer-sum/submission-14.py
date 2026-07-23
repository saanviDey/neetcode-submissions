class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            l = i + 1
            r = len(sorted_nums) - 1
            while l < r:
                if sorted_nums[l] + sorted_nums[r] < -sorted_nums[i]:
                    l += 1
                elif sorted_nums[l] + sorted_nums[r] > -sorted_nums[i]:
                    r -= 1
                else:
                    result.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    while sorted_nums[l] == sorted_nums[l - 1] and l < r:
                        l += 1
        
        return result

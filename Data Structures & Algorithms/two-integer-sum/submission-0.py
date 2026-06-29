class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, num in enumerate(nums):
            diff_num = target - num
            if diff_num in diff:
                return [diff[diff_num], i]
            diff[num] = i
        return
        
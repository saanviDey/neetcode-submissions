class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        # use a hashset
        # key : val -> num : index
        # add the num if the difference doesn't exist
        # check if target - num already exists in the hashset
        # the diff will exist once we reach a number later in the array
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i
        return
        
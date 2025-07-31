class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for index, num in enumerate(nums):
            x = target - num
            if x in seen:
                return [seen[x], index]
            seen[num]=index
        
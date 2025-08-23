class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums)!=len(nums):
            return max(nums)+1
        
        else:
            for i in range(0,max(nums)):
                if i not in nums:
                    return i

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        k=len(nums)
        for i in range(k):
            if target == nums[i]:
                return i
            elif target<nums[i]:
                return i
            elif target > nums[k-1]:
                return k
                

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        write = 0
        for x in nums:
            if x != 0:
                nums[write] = x
                write += 1
        for i in range(write, len(nums)):
            nums[i] = 0



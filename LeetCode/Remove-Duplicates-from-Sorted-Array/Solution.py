class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=1
        i = 0
        while len(nums)-1>i:
            if nums[i] != nums[i+1]:
                k+=1
                i+=1
            else:
                nums.pop(i+1)
        return k
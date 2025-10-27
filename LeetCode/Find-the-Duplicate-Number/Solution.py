class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mos=set()
        for i in nums:
            if i not in mos:
                mos.add(i)
            else:
                return i
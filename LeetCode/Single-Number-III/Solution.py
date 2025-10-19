class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        mydict=collections.Counter(nums)

        mydict={k:v for k,v in mydict.items() if v==1}

        ans=list(mydict.keys())
        return ans
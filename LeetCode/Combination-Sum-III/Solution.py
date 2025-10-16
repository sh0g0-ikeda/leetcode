class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[]

        def ooo(start,path,total):
            if len(path)==k:
                if total==n:
                    ans.append(path)
                return

            for i in range(start,10):
                ooo(i+1,path+[i],total+i)
        ooo(1,[],0)
        return ans
                

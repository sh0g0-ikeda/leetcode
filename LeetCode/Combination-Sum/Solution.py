class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]

        def calc(current,path):

            #終了条件
            if sum(path)==target:
                ans.append(path)
                return
            if sum(path)>target:
                return
            
            if sum(path)<target:
                for i in range(current,len(candidates)):
                    calc(i,path+[candidates[i]])

        calc(0,[])
        return ans
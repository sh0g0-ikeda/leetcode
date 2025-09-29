class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans=[]


        if len(digits)==0:
            return []
        nums={'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        def ooo(current,path):

            if current==len(digits): #終了条件
                ans.append(path)
                return

            curdig=digits[current]
            let=nums[curdig]

            for i in let:
                ooo(current+1,path+i)

        ooo(0,'')
        return ans


        
                



        

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[]
        for _ in range(n):
            ans.append([0]*n)


        top=0
        btm=n-1
        left=0
        right=n-1
        cnt=1

        while left <= right and top <= btm:

            for i in range(left,right+1):
                ans[top][i]=cnt
                cnt+=1
            top+=1

            
            for j in range(top,btm+1):
                ans[j][right]=cnt
                cnt+=1
            right-=1

            
            if top <= btm:
                for k in range(right,left-1,-1):
                    ans[btm][k]=cnt
                    cnt+=1
                btm-=1

            if left<=right:
                for l in range(btm,top-1,-1):
                    ans[l][left]=cnt
                    cnt+=1
                left+=1

        return ans




            

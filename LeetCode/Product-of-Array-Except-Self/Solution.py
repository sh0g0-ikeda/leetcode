1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        
4        ans=[1]*len(nums)
5
6        left=1
7        for i in range(len(nums)):
8            ans[i]=left
9            left*=nums[i]
10        right=1
11        for j in range(len(nums)-1, -1, -1):
12            ans[j]*=right
13            right*=nums[j]
14
15        return ans
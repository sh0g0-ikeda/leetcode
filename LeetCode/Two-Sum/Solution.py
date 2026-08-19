1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        k=len(nums)
4        ans=[]
5        for i in range(k):
6            for j in range(i+1, k):
7                if nums[i]+nums[j]==target:
8                    ans.append(i)
9                    ans.append(j)
10
11        return ans
12
13
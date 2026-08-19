1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        seen = {}
4        for i, num in enumerate(nums):
5            need = target-num
6
7            if need in seen:
8                return [seen[need], i]
9
10            seen[num]=i
11
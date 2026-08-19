1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        seen=set()
4        for i in nums:
5            if i in seen:
6                return True
7            seen.add(i)
8
9        return False
10
11
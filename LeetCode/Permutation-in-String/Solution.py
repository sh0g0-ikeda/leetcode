1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        n=len(s1)
4
5        for i in range(len(s2)-n+1):
6            if sorted(s1)==sorted(s2[i:i+n]):
7                return True
8        return False
9
10
11
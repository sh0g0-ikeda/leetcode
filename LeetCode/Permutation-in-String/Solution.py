1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        n=len(s1)
4        for l in range(len(s2)-n+1):
5            if sorted(s1)==sorted(s2[l: l+n]):
6                return True
7        return False
8
9
10
11
12
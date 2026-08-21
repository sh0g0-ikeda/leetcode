1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        left=1
4        right=max(piles)
5
6        while right>left:
7            center=(left+right)//2
8            total=0
9            for i in piles:
10                total+=(i+center-1)//center
11            if h>=total:
12                right=center
13
14            elif h<total:
15                left=center+1
16        return left
17
18
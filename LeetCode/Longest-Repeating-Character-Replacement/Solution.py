1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        l=0
4        count = {}
5        maxf=0
6        ans=0
7        
8        for r in range(len(s)):
9            count[s[r]]=count.get(s[r], 0)+1
10            maxf=max(maxf, count[s[r]])
11
12            while (r-l+1)-maxf>k:
13                count[s[l]]-=1
14                l+=1
15            ans=max(ans, r-l+1)
16
17        return ans
18
19            
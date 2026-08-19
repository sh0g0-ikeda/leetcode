1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        
4        groups={}
5
6        for i in strs:
7            key="".join(sorted(i))
8            if key not in groups:
9                groups[key]=[]
10            groups[key].append(i)
11
12        return list(groups.values())
13
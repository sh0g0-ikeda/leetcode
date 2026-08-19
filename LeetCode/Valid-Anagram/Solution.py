1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        seen1={}
4        seen2={}
5        for i in s:
6            if i not in seen1:
7                seen1[i]=1
8            else:
9                seen1[i]+=1
10
11        for j in t:
12            if j not in seen2:
13                seen2[j]=1
14            else:
15                seen2[j]+=1
16        if seen1==seen2:
17            return True
18        else:
19            return False
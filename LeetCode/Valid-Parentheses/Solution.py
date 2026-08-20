1class Solution:
2    def isValid(self, s: str) -> bool:
3        cnt={"}":"{", ")":"(", "]":"["}
4        stack=[]
5
6        for i in range(len(s)):
7            if s[i] in "[{(":
8                stack.append(s[i])
9            else:
10                if not stack or cnt[s[i]]!=stack[-1]:
11                    return False
12                stack.pop()
13        
14        
15        return len(stack)==0
16
17
18
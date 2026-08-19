1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        clean = ""
4
5        for c in s:
6            if c.isalnum():
7                clean += c.lower()
8        n=len(clean)
9        m=len(clean)//2
10        for i in range(m):
11            if clean[i] != clean[n-1-i]:
12                return False
13
14        return True
15
16
17            
18
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        group = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in group.values():
                stack.append(char)
            elif char in group:
                if not stack or group[char]!=stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack




            

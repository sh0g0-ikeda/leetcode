class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            xstr = str(x)
            for i in range(len(xstr) // 2):  # 半分だけでOK
                if xstr[i] != xstr[-i - 1]:
                    return False
            return True
        
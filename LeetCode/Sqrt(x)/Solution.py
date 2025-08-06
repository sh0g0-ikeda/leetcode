class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        m=''
        for i in range(2**16):
            if i * i > x:
                return i - 1
        return 2**16 - 1  # これがx=2^31-1のとき最大値
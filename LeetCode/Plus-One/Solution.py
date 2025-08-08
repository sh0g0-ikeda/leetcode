class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=1
        i = len(digits)-1
        while i>=0:
            digits[i] += carry
            if digits[i]==10:
                digits[i]=0
                carry=1
                if i ==0:
                    digits.insert(0, 1)
            else:
                carry=0
            i -=1

        return digits


             
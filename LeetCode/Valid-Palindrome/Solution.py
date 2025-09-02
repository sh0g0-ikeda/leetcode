class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        test=reversed(s)
        if test==s:
            return True

        snew= "".join(ch for ch in s if ch.isalnum())
        snew=snew.lower()
        srev=''.join(reversed(snew))

        if snew==srev:
            return True
        else:
            return False


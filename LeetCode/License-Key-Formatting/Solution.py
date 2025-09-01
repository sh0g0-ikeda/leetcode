class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s2=s.replace('-','').upper()
        first=len(s2)%k or k
        parts=[s2[:first]]
        for i in range(first, len(s2), k):
            parts.append(s2[i:i+k])
        return '-'.join(parts)

            
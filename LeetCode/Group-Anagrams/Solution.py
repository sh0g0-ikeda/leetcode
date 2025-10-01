class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic={}
        for i in strs:
            x=sorted(i)
            key=''.join(x)
            if key not in dic:
                dic[key]=[]
            dic[key].append(i)
        ans=list(dic.values())
        return ans


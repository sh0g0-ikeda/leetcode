class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        cmpr=[]
        W=1
        mos=set()
        while W<=(area/W):
            if area%W==0:
                cmpr.append([area/W, W])
                W+=1
            else:
                W+=1
        for i in cmpr:
            mos.add(i[0]-i[1])
            if min(mos)>=(i[0]-i[1]):
                j=i
        return j

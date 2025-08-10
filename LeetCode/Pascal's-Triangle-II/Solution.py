class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            for i in range(len(row)-1, 0, -1):
                s = row[i] + row[i-1]
                row.insert(i, s)  
                row.pop(i+1)      
            row.append(1)
        return row
    

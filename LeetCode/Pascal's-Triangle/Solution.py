class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 0:
            return []

        row = [1]
        output = [row[:] ]  

        for _ in range(1, numRows):
            for i in range(len(row)-1, 0, -1):  
                row[i] = row[i] + row[i-1]
            row.append(1)                        
            output.append(row[:])                

        return output

    

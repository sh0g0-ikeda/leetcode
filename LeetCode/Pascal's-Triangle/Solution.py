class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 0:
            return []

        row = [1]
        output = [row[:] ]  # 0行目

        for _ in range(1, numRows):
            for i in range(len(row)-1, 0, -1):   # 右から更新
                row[i] = row[i] + row[i-1]
            row.append(1)                         # 末尾の1
            output.append(row[:])                 # ここはコピーを入れる

        return output

    

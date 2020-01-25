class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return 
        
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        row_start = 0
        row_end = row_len - 1
        col_start = 0
        col_end = col_len - 1
        
        ret = []
        
        while row_start <= row_end and col_start <= col_end:
            
            for i in range(col_start, col_end + 1):
                ret.append(matrix[row_start][i])
                
            row_start += 1
            
            for j in range(row_start, row_end + 1):
                ret.append(matrix[j][col_end])
            
            col_end -= 1 
            
            if row_start <= row_end:
                for l in range(col_end, col_start - 1, -1):
                    ret.append(matrix[row_end][l])

            row_end -= 1
            
            if col_start <= col_end:
                for k in range(row_end, row_start - 1, -1):
                    ret.append(matrix[k][col_start])

            col_start += 1
        
        return ret
            
            

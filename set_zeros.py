class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        mark = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    mark.append((i,j))
        
        for pair in mark:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if pair[0] == i or pair[1] == j:
                        matrix[i][j] = 0
                    

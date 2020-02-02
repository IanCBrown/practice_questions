class Solution:
    def isToeplitzMatrix(self, matrix):
        flag = True
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if col > 0 and row > 0:
                    print(matrix[row][col])
                    if matrix[row - 1][col - 1] != matrix[row][col]:
                        flag = False
                    
        return flag
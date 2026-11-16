class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.Nmatrix = matrix
        for i in range(1,len(matrix[0])):
            self.Nmatrix[0][i] = matrix[0][i-1] + matrix[0][i]
        for i in range(1,len(matrix)):
            self.Nmatrix[i][0] = matrix[i-1][0]+matrix[i][0]
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                self.Nmatrix[i][j] = matrix[i][j]+ matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.Nmatrix[row2][col2] 
        
        if row1-1 >= 0 and col1-1 >=0:
            ans -= self.Nmatrix[row2][col1-1]
            ans -= self.Nmatrix[row1-1][col2]
            ans += self.Nmatrix[row1-1][col1-1]
        elif row1-1 >= 0:
            ans -= self.Nmatrix[row1-1][col2]
        elif col1-1 >=0:
            ans -= self.Nmatrix[row2][col1-1]
        return ans




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
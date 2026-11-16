class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        ans = [[[] for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    ans[i][j]  = matrix[0][0]
                if i == 0 and j > 0:
                    ans[i][j]  = ans[i][j-1] + matrix[i][j] 
                if i > 0 and j == 0:
                    ans[i][j]  = ans[i-1][j] + matrix[i][j]
                if i > 0 and j > 0:
                    ans[i][j] = ans[i-1][j] + ans[i][j-1] - ans[i-1][j-1] + matrix[i][j]
        self.matrix = ans

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        if row1 == 0 and col1 > 0:
            return self.matrix[row2][col2]-self.matrix[row2][col1-1]
        if row1 > 0 and col1 == 0:        
            return self.matrix[row2][col2]-self.matrix[row1-1][col2]
        if row1 > 0 and col1 > 0:
            return self.matrix[row2][col2]-self.matrix[row2][col1-1]-self.matrix[row1-1][col2]+self.matrix[row1-1][col1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
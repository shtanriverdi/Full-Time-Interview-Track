class NumMatrix:
    prefix = None
    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix) + 1
        cols = len(matrix[0]) + 1
        NumMatrix.prefix = [ [0] * cols for _ in range(rows) ]
        for i in range(1, rows):
            for j in range(1, cols):
                NumMatrix.prefix[i][j] = matrix[i - 1][j - 1]
                NumMatrix.prefix[i][j] += NumMatrix.prefix[i - 1][j] + NumMatrix.prefix[i][j - 1] - NumMatrix.prefix[i - 1][j - 1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        upper = NumMatrix.prefix[row1][col2 + 1]
        left = NumMatrix.prefix[row2 + 1][col1]
        upper_left = NumMatrix.prefix[row1][col1]
        right_corner = NumMatrix.prefix[row2 + 1][col2 + 1]
        return right_corner - upper - left + upper_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
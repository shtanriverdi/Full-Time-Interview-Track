class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        for i in range(1, N):
            for j in range(N):
                upper_left = matrix[i - 1][j - 1] if (j - 1 >= 0) else float("inf")
                up = matrix[i - 1][j]
                upper_right = matrix[i - 1][j + 1] if (j + 1 < N) else float("inf")
                matrix[i][j] += min(upper_left, up, upper_right)
                
        return min(matrix[-1])
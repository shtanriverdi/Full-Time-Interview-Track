class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        for row in range(1, N):
            matrix[0].extend(matrix[row])
            
        matrix[0].sort()
        
        return matrix[0][k - 1]

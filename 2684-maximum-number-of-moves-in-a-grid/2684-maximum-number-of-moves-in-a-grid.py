class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        dp = [ [0]*N for _ in range(M) ]
        
        for col in range(N - 2, -1, -1):
            for row in range(M):
                # Upper-right
                if row - 1 >= 0 and grid[row - 1][col + 1] > grid[row][col]:
                    dp[row][col] = max(dp[row - 1][col + 1] + 1, dp[row][col])
                # Right
                if grid[row][col + 1] > grid[row][col]:
                    dp[row][col] = max(dp[row][col + 1] + 1, dp[row][col])
                # Lower-right
                if row + 1 < M and grid[row + 1][col + 1] > grid[row][col]:
                    dp[row][col] = max(dp[row + 1][col + 1] + 1, dp[row][col])
                    
                # for i in range(M):
                #     for j in range(N):
                #         print(dp[i][j], end=" ")
                #     print()
                # print()
        
        answer = 0
        for i in range(M):
            answer = max(answer, dp[i][0])
            
        return answer
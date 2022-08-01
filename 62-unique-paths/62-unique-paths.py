class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m += 1
        n += 1
        
        dp = [ [0]*n for _ in range(m) ]
        dp[1][1] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += dp[i][j - 1] + dp[i - 1][j]
        
        return dp[-1][-1]
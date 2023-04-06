class Solution:
    def isInside(self, i, j, M, N):
        if i < 0 or i == M or j < 0 or j == N:
            return False
        return True
    
    def isNotOnBorder(self, i, j, M, N):
        if i == 0 or i == M - 1 or j == 0 or j == N - 1:
            return False
        return True
    
    def dfs(self, i, j, M, N, grid, directions):
        grid[i][j] = 1
        isSafe = self.isNotOnBorder(i, j, M, N)
        for direction in directions:
            ni = i + direction[0]
            nj = j + direction[1]
            if self.isInside(ni, nj, M, N) and grid[ni][nj] == 0:
                isSafe &= self.dfs(ni, nj, M, N, grid, directions)
                
        return isSafe
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        count = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    count += self.dfs(i, j, M, N, grid, directions)
                    
        return count
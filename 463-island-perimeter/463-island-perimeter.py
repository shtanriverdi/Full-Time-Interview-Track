class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        
        directions = [1, 0, -1, 0, 1]
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    return self.dfs(i, j, M, N, grid, directions)
        
    def dfs(self, i, j, M, N, grid, directions):
        
        # Mark current cell as visited
        grid[i][j] = 2
        
        perimeter = 0
        
        # Check for 4 directions
        for d in range(4):
            ni = i + directions[d]
            nj = j + directions[d + 1]
            is_inside = self.inside(ni, nj, M, N)
            if is_inside and grid[ni][nj] == 1:
                perimeter += self.dfs(ni, nj, M, N, grid, directions)
            elif not is_inside or grid[ni][nj] != 2:
                perimeter += 1
        
        return perimeter
        
        
    def inside(self, i, j, M, N):
        if i < 0 or i >= M or j < 0 or j >= N:
            return False
        return True
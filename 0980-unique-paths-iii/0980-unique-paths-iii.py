class Solution:
    def dfs(self, i, j, M, N, grid, directions, total_cell_count, seen_cell_count, num_of_valid_paths):
        prev_cell = grid[i][j]
        seen_cell_count += 1
        
        if grid[i][j] == 2 and seen_cell_count == total_cell_count:
            num_of_valid_paths[0] += 1
        
        grid[i][j] = -1
        
        for direction in directions:
            ni = i + direction[0]
            nj = j + direction[1]
            if ni >= 0 and ni < M and nj >= 0 and nj < N and grid[ni][nj] != -1:
                self.dfs(ni, nj, M, N, grid, directions, total_cell_count, seen_cell_count, num_of_valid_paths)
            
        seen_cell_count -= 1
        grid[i][j] = prev_cell
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        start = [-1, -1]
        block_count = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == -1:
                    block_count += 1
                if grid[i][j] == 1:
                    start = [i, j]
        
        num_of_valid_paths = [0]
        total_cell_count = (M * N) - block_count
        self.dfs(start[0], start[1], M, N, grid, directions, total_cell_count, 0, num_of_valid_paths)
        
        return num_of_valid_paths[0]
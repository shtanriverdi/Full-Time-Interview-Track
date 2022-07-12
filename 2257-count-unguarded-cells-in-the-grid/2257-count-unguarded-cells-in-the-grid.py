class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [ [0]*n for _ in range(m) ]
        
        for w_i, w_j in walls:
            grid[w_i][w_j] = 1
        
        for g_i, g_j in guards:
            grid[g_i][g_j] = 1

        directions = [0, 1, 0, -1, 0]
        for g_i, g_j in guards:
            self.dfs(g_i, g_j, m, n, grid, directions)
            
        # for i in range(m):
        #     for j in range(n):    
        #         print(grid[i][j],end=" ")
        #     print("")
        
        safe_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    safe_count += 1
                    
        return safe_count
    
    def dfs(self, g_i, g_j, m, n, grid, directions):
        for dir_index in range(1, 5):
            direction = (directions[dir_index], directions[dir_index - 1])
            self.goToGivenDirection(g_i, g_j, m, n, direction, grid)
        
    def goToGivenDirection(self, cur_i, cur_j, m, n, direction, grid):
        cur_i += direction[0]
        cur_j += direction[1]
        while self.inside(cur_i, cur_j, m, n) and (grid[cur_i][cur_j] != 1):
            grid[cur_i][cur_j] = -1
            cur_i += direction[0]
            cur_j += direction[1]
        
    def inside(self, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        return True
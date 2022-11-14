class Solution:
    def dfs(self, i, j, line_map_x, line_map_y, visited_coordinates, answer):
        visited_coordinates.add( (i, j) )
        for (x_i, x_j) in line_map_x[i]:
            if (x_i, x_j) not in visited_coordinates:
                answer[0] += 1
                self.dfs(x_i, x_j, line_map_x, line_map_y, visited_coordinates, answer)
                
        for (y_i, y_j) in line_map_y[j]:
            if (y_i, y_j) not in visited_coordinates:
                answer[0] += 1
                self.dfs(y_i, y_j, line_map_x, line_map_y, visited_coordinates, answer)
        
    
    def removeStones(self, stones: List[List[int]]) -> int:
        line_map_x = defaultdict(set)
        line_map_y = defaultdict(set)
        
        for i, j in stones:
            line_map_x[i].add( (i, j) )
            line_map_y[j].add( (i, j) )
        
        visited_coordinates = set()
        answer = [0]
        for i, j in stones:
            self.dfs(i, j, line_map_x, line_map_y, visited_coordinates, answer)
            
        return answer[0]
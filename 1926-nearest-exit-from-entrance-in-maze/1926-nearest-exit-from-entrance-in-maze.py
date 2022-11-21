class Solution:
    def nearestExit(self, maze: List[List[str]], start: List[int]) -> int:
        M = len(maze)
        N = len(maze[0])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        todo = deque()
        todo.append([start[0], start[1], 0])
        maze[start[0]][start[1]] = '+'
        
        while todo:
            cur_x, cur_y, steps = todo.popleft()
            for direction in directions:
                nx = cur_x + direction[0]
                ny = cur_y + direction[1]
                if nx >= 0 and nx < M and ny >= 0 and ny < N and maze[nx][ny] == '.':
                    todo.append([nx, ny, steps + 1])
                    maze[nx][ny] = '+'
                    if nx == 0 or nx == M - 1 or ny == 0 or ny == N - 1:
                        return steps + 1
                    
        return -1
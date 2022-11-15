class Solution:
    def neighborCounter(self, i, j, M, N, directions, board):
        dead_count = 0
        live_count = 0
        for direction in directions:
            ni = i + direction[0]
            nj = j + direction[1]
            if ni >= 0 and ni < M and nj >= 0 and nj < N:
                if board[ni][nj] == 1:
                    live_count += 1
                else:
                    dead_count += 1
        return [live_count, dead_count]
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        M = len(board)
        N = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        states_todo = []
        for i in range(M):
            for j in range(N):
                live_count, dead_count = self.neighborCounter(i, j, M, N, directions, board)
                # Dead cell
                if board[i][j] == 0:
                    if live_count == 3:
                        states_todo.append([i, j, 1])
                # Live cell
                else:
                    status = 1
                    if live_count < 2 or live_count > 3:
                        status = 0
                    states_todo.append([i, j, status])
        
        for x, y, state in states_todo:
            board[x][y] = state
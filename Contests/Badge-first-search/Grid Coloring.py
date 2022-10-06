class Solution:
    def bfs(self, i, j, M, N, dirs, matrix, original_color):
        todo = deque()
        covered_cell_count = 1
        todo.append([0, 0])
        matrix[i][j] = 1 ^ matrix[i][j]
        while todo:
            cur_i, cur_j = todo.popleft()
            for d in range(1, 5):
                ni = cur_i + dirs[d]
                nj = cur_j + dirs[d - 1]
                if (ni >= 0 and ni < M and nj >= 0 and nj < N) and matrix[ni][nj] == original_color:
                    todo.append([ni, nj])
                    matrix[ni][nj] = 1 ^ matrix[ni][nj]
                    covered_cell_count += 1
        return covered_cell_count

    def solve(self, matrix):
        M = len(matrix)
        N = len(matrix[0])
        total_cells = M * N

        dirs = [0, 1, 0, -1, 0]
        answer = 0

        count = self.bfs(0, 0, M, N, dirs, matrix, matrix[0][0])
        while count != total_cells:
            count = self.bfs(0, 0, M, N, dirs, matrix, matrix[0][0])
            answer += 1

        return answer
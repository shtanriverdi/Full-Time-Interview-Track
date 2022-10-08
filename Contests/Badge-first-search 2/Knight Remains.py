class Solution:
    def dfs(self, dirs, x, y, N, k, memo):
        if x < 0 or x >= N or y < 0 or y >= N:
            return 0

        if k == 0:
            return 1

        if (x, y, k) in memo:
            return memo[(x, y, k)]

        answer = 0
        for direction in dirs:
            nx = x + direction[0]
            ny = y + direction[1]
            answer += self.dfs(dirs, nx, ny, N, k - 1, memo)

        memo[(x, y, k)] = answer
        return answer

    def solve(self, n, x, y, k):
        answer = 0
        posses = 0
        memo = {}
        dirs = [ [-2, 1], [-2, -1], [2, 1], [2, -1], [-1, 2], [1, 2], [-1, -2], [1, -2] ]
        posses += self.dfs(dirs, x, y, n, k, memo)
        answer = posses / (8**k) * 100
        return int(answer)
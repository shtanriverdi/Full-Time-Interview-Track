import sys
input = sys.stdin.readline

def isInside(i, j, M, N):
    if i < 0 or i == M or j < 0 or j == N:
        return False
    return True

def hasCornerOrHashtag(i, j, M, N, grid, directions):
    for direction in directions:
        ni = i + direction[0]
        nj = j + direction[1]
        if isInside(ni, nj, M, N) == False:
            return True
        if isInside(ni, nj, M, N) and grid[ni][nj] == '#':
            return True
    return False

def main():
    M, N = list(map(int, input().split()))
    grid = []
    for _ in range(M):
        line = input().rstrip()
        grid.append( line )

    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    answer = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == '.':
                hasAnyAround = hasCornerOrHashtag(i, j, M, N, grid, dirs)
                if hasAnyAround:
                    answer += 1

    print(answer)


if __name__ == "__main__":
    main()

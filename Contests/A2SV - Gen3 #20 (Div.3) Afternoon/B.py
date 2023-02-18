import sys
input = sys.stdin.readline

def isInside(i, j, rows, cols):
    if i < 0 or i == rows or j < 0 or j == cols:
        return False
    return True

def hasWolfNearby(i, j, grid, rows, cols, directions):
    for direction in directions:
        ni = i + direction[0]
        nj = j + direction[1]
        if isInside(ni, nj, rows, cols):
            if grid[ni][nj] == 'W':
                return True
            elif grid[ni][nj] == '.':
                grid[ni][nj] = 'D'

    return False

def main():
    rows, cols = list(map(int, input().split()))
    grid = []

    for _ in range(rows):
        line = [ *input().strip() ]
        grid.append( line )

    possible = True
    directions = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                hasWolf = hasWolfNearby(i, j, grid, rows, cols, directions)
                if hasWolf:
                    possible = False
                    break

    if possible:
        print("Yes")
        for i in range(rows):
            print("".join(grid[i]))
    else:
        print("No")


if __name__ == "__main__":
    main()

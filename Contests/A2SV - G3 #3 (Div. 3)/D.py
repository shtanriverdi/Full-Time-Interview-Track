import sys
input = sys.stdin.readline

def fallTheStone(i, j, rows, cols, grid):
    i += 1
    while i < rows and grid[i][j] == '.':
        grid[i - 1][j] = '.'
        grid[i][j] = '*'
        i += 1

def main():
    t = int(input())
    for _ in range(t):
        rows, cols = list(map(int, input().split()))
        grid = []
        for i in range(rows):
            current_row = [ *input().strip() ]
            grid.append(current_row)

        for ith_row in reversed(range(rows)):
            for jth_col in range(cols):
                if grid[ith_row][jth_col] == '*':
                    fallTheStone(ith_row, jth_col, rows, cols, grid)
        
        for ith_row in range(rows):
            print("".join(grid[ith_row]))
        print("")

if __name__ == "__main__":
    main()
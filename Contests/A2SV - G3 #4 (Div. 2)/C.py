import sys
from collections import defaultdict, deque
input = sys.stdin.readline

sys.setrecursionlimit(10000)

def dfs(i, j, n, m, grid, start_i, start_j, start_letter, nodes_count, dirs):

    prev_letter = grid[i][j]
    grid[i][j] = '*'

    answer = False

    for d in range(1, 5):

        ni = i + dirs[d]
        nj = j + dirs[d - 1]

        if ni == start_i and nj == start_j and nodes_count + 1 >= 4:
            return True

        if (ni >= 0 and ni < n and nj >= 0 and nj < m) and start_letter == grid[ni][nj]:
            answer = dfs(ni, nj, n, m, grid, start_i, start_j, start_letter, nodes_count + 1, dirs)
            if answer:
                break


    grid[i][j] = prev_letter
    return answer

def main():
    n, m = list(map(int, input().split()))
    
    grid = []
    for _ in range(n):
        row = [ *input().strip() ]
        grid.append( row )

    dirs = [0, 1, 0, -1, 0]
    
    for i in range(n):
        for j in range(m):
            is_possible = dfs(i, j, n, m, grid, i, j, grid[i][j], 0, dirs)
            if is_possible:
                print("Yes")
                sys.exit(0)

    print("No")

if __name__ == "__main__":
    main()
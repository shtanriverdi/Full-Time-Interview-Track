import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

def main():
    n, m = list(map(int, input().split()))

    grid = []
    for _ in range(n):
        row = [ *input().strip() ]
        grid.append( row )

    row_map = defaultdict(lambda: defaultdict(int))
    col_map = defaultdict(lambda: defaultdict(int))

    for i in range(n):
        for j in range(m):
            char = grid[i][j]
            row_map[i][char] += 1
            col_map[j][char] += 1

    encrypted = []
    for i in range(n):
        for j in range(m):
            char = grid[i][j]
            row_count = row_map[i][char]
            col_count = col_map[j][char]
            if row_count == 1 and col_count == 1:
                encrypted.append( char )

    print("".join(encrypted))


if __name__ == "__main__":
    main()

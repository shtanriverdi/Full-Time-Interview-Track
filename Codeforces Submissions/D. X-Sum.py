import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):

        row, col = list(map(int, input().split()))
        grid = []
        for i in range(row):
            nums = list(map(int, input().split()))
            grid.append( nums )

        diagonal_1_sum_map = defaultdict(int)
        diagonal_2_sum_map = defaultdict(int)
        for i in range(row):
            for j in range(col):
                diagonal_1_key = i + j
                diagonal_2_key = i - j
                diagonal_1_sum_map[diagonal_1_key] += grid[i][j]
                diagonal_2_sum_map[diagonal_2_key] += grid[i][j]

        max_cross_sum = 0
        for i in range(row):
            for j in range(col):
                diagonal_1_key = i + j
                diagonal_2_key = i - j
                diagonal_1_sum = diagonal_1_sum_map[diagonal_1_key]
                diagonal_2_sum = diagonal_2_sum_map[diagonal_2_key]
                total_digonal_sum = diagonal_1_sum + diagonal_2_sum - grid[i][j]
                max_cross_sum = max(max_cross_sum, total_digonal_sum)

        print(max_cross_sum)


if __name__ == "__main__":
    main()

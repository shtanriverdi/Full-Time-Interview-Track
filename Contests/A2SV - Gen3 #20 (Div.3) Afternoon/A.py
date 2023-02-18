import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        grid = []

        cols = int(input())

        row_1 = [ *input().strip() ]
        row_2 = [ *input().strip() ]

        grid = [ row_1, row_2 ]
        
        answer = [ [0]*cols for _ in range(2) ]

        answer[0][0] = 1

        for j in range(1, cols):
            if grid[0][j] == '0' and ((answer[0][j - 1] == 1 and grid[0][j - 1] == '0') or (answer[1][j - 1] == 1 and grid[1][j - 1] == '0')):
                answer[0][j] = 1

            if grid[1][j] == '0' and ((answer[1][j - 1] == 1 and grid[1][j - 1] == '0') or (answer[0][j - 1] == 1 and grid[0][j - 1] == '0')):
                answer[1][j] = 1

        if answer[-1][-1] == 1:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()

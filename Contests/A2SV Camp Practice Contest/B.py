import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(cur, destination, path):
    path.append(cur)

    if cur > destination:
        path.pop()
        return False

    if cur == destination:
        return True

    possible_ans_1 = dfs(cur * 2, destination, path)
    if possible_ans_1:
        return True

    possible_ans_2 = dfs((cur * 10) + 1, destination, path)
    if possible_ans_2:
        return True

    path.pop()


def main():
    A, B = list(map(int, input().split()))

    path = []
    hasFound = dfs(A, B, path)

    if hasFound:
        print("YES")
        print(len(path))
        for p in path:
            print(p, end=" ")
    else:
        print("NO")
        

if __name__ == "__main__":
    main()
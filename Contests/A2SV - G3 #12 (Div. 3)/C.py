import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):

        n, a, b = list(map(int, input().split()))

        if n == a and a == b:
            print("Yes")
            continue

        middle_len = n - a - b
        if middle_len >= 2:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
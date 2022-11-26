import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    n = int(input())
    portions = list(map(int, input().split()))

    orange = 0
    for portion in portions:
        orange += portion / 100

    print((orange / n) * 100)

if __name__ == "__main__":
    main()
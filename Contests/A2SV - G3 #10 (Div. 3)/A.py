import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_sum_or = 0
    for num in A:
        A_sum_or = (A_sum_or | num)

    B_sum_or = 0
    for num in B:
        B_sum_or = (B_sum_or | num)

    print(A_sum_or + B_sum_or)

if __name__ == "__main__":
    main()
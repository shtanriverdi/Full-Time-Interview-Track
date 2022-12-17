import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):

        size = int(input())
        nums = list(map(int, input().split()))

        min_num = min(nums)
        if min_num == nums[0]:
            print("Bob")
        else:
            print("Alice")


if __name__ == "__main__":
    main()
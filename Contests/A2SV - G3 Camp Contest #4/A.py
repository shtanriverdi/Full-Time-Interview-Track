import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    n = int(input())
    heights = [0] + list(map(int, input().split()))

    energy = 0
    cost = 0

    for i in range(1, n + 1):
        energy += heights[i - 1] - heights[i]
        if energy < 0:
            cost += abs(energy)
            energy = 0

    print(cost)
        

if __name__ == "__main__":
    main()
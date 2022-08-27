import sys
from collections import Counter
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        problems = input().strip()

        counts = Counter(problems)
        answer = len(counts) + sum(counts.values())
        print(answer)

if __name__ == "__main__":
    main()
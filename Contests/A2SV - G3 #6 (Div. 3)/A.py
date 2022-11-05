import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.append(float("-inf"))

    stack = []
    answer = -1

    for num in nums:
        if stack and num < stack[-1]:
            answer = max(answer, len(stack))
            stack = []

        stack.append(num)

    print(answer)
        

if __name__ == "__main__":
    main()
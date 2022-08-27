import sys
from collections import Counter
input = sys.stdin.readline

def main():
    n = int(input())
    levels = [False] * (n + 1)

    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    for i in range(1, len(x)):
        levels[x[i]] = True
    for i in range(1, len(y)):
        levels[y[i]] = True

    answer = True
    for i in range(1, n + 1):
        if levels[i] == False:
            answer = False
            break

    if answer == True:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")


if __name__ == "__main__":
    main()
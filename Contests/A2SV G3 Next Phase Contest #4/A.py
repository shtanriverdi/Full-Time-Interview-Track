import sys
from collections import Counter
input = sys.stdin.readline

def main():
    n = int(input())
    word = input().strip().lower()
    counts = Counter(word)

    numOfLetters = len(counts)
    if numOfLetters == 26:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
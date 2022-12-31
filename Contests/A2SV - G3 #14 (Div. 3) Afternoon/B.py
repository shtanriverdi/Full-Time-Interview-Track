import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

def main():
    n, m = list(map(int, input().split()))

    poland_set = set()
    for _ in range(n):
        word = str(input().strip())
        poland_set.add( word )

    common_words = set()
    for _ in range(m):
        word = str(input().strip())
        if word in poland_set:
            common_words.add( word )

    common_word_count = len(common_words)

    if n > m:
        print("YES")
    elif m > n:
        print("NO")
    # m == n
    else:
        if common_word_count % 2 == 0:
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    main()

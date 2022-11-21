import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    n = int(input())
    letters = [ *input().strip() ]

    letter_map = defaultdict(int)
    for letter in letters:
        letter_map[letter.lower()] += 1

    alp_size = len(letter_map)
    if alp_size == 26:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
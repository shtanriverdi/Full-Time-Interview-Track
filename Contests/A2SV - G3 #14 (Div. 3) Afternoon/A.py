import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

def main():
    word = str(input().strip())

    max_value = ord(max(word))
    answer = []
    for char in word:
        char_value = ord(char)
        if char_value == max_value:
            answer.append( char )

    print("".join(answer))


if __name__ == "__main__":
    main()

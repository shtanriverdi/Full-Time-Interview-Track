import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):

        size = int(input())
        string = input()

        max_letter = max(string)
        print(ord(max_letter) - 96)

if __name__ == "__main__":
    main()
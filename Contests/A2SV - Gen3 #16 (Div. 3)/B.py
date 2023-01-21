import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split()))

        is_even_Up = (n % 2 == 0)
        is_even_Right = (m % 2 == 0)

        # Even Even
        if is_even_Up == True and is_even_Right == True:
            print("Tonya")
        elif is_even_Up == False and is_even_Right == False:
            print("Tonya")
        else:
            print("Burenka")


if __name__ == "__main__":
    main()

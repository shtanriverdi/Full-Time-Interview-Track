import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):

        digits = input().strip()
        n = len(digits)

        if n < 3:
            print(0)
            continue

        left = 0
        window_map = defaultdict(int)

        ans = 200001

        for right in range(n):
            window_map[ digits[right] ] += 1
            while len(window_map) == 3:
                win_len = right - left + 1
                ans = min(ans, win_len)
                window_map[ digits[left] ] -= 1
                if window_map[ digits[left] ] == 0:
                    window_map.pop(digits[left])
                left += 1

        if ans == 200001:
            ans = 0

        print(ans)


if __name__ == "__main__":
    main()
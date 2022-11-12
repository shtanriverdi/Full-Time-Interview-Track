import sys
import heapq
from collections import defaultdict
from collections import Counter
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, current_color = list(input().split())
        color_part_1 = [ *input().strip() ]
        n = int(n)
        colors = color_part_1 + color_part_1

        if current_color == 'g':
            print(0)
            continue

        # Find green from right to left most
        green_index = 0
        while green_index < n and colors[green_index] != 'g':
            green_index += 1
        green_index += n

        # To left
        answer = 0
        cur_index = green_index
        while cur_index >= 0:
            if colors[cur_index] == current_color:
                diff = green_index - cur_index
                answer = max(answer, diff)

            # Update green index
            elif colors[cur_index] == 'g':
                green_index = cur_index

            cur_index -= 1

        print(answer)

if __name__ == "__main__":
    main()
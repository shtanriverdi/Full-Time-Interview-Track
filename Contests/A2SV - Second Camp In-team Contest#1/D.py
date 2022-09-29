import sys
input = sys.stdin.readline

def main():
    n = int(input())
    heights = list(map(int, input().split()))

    # Index, Height
    last_updated = [ -1, -1 ]

    boxes = int(input())
    for _ in range(boxes):
        answer = -1

        wi, hi = list(map(int, input().split()))
        wi -= 1

        last_index = last_updated[0]
        last_height = last_updated[1]

        answer = max(last_height, heights[wi])
        
        # Update Last
        last_updated[0] = wi
        last_updated[1] = answer + hi

        print(answer)


if __name__ == "__main__":
    main()
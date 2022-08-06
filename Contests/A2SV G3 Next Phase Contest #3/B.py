import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))


        # Find first on zero index
        first_nonzero_idx = float("inf")
        for i in range(0, n - 1):
            if nums[i] != 0:
                first_nonzero_idx = i
                break

        if first_nonzero_idx == float("inf"):
            print("0")
            continue

        last_nonzero_idx = -1
        for i in range(n - 1, -1, -1):
            if nums[i] != 0:
                last_nonzero_idx = i
                break

        nonzero_sum = 0
        zero_count = 0
        for i in range(first_nonzero_idx, n - 1):
            if nums[i] == 0:
                zero_count += 1
            else:
                nonzero_sum += nums[i]

        if nonzero_sum == 0:
            print("0")
            continue

        print(nonzero_sum + zero_count)


if __name__ == "__main__":
    main()
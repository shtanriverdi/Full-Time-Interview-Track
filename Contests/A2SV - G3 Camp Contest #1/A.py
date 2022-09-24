import sys
input = sys.stdin.readline

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    count = 0
    for i in range(1, n - 1):
        if nums[0] < nums[i] and nums[-1] > nums[i]:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
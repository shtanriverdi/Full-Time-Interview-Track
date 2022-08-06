import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        biggest = nums[-1]

        a, b = nums[0], nums[1]
        missing_sum = a + b
        for i in range(2, 7):
            if nums[i] + missing_sum == biggest:
                print(a, b, nums[i])
                break

if __name__ == "__main__":
    main()
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    right_index = 0
    left_index = 0

    answer = 1

    for right_index in range(n):
        current_diff = nums[right_index] - nums[left_index]
        if current_diff > 5:
            left_index += 1
        else:
            window_len = right_index - left_index + 1
            answer = max(answer, window_len)

    print(answer)


if __name__ == "__main__":
    main()
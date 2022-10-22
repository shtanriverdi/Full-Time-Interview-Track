import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    length, k = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    numbers.sort()

    left_index = 0

    answer_frequency = 1
    answer_number = numbers[0]

    window_sum = k

    for right_index in range(0, length):
        window_len = right_index - left_index + 1
        window_sum += numbers[right_index]
        average = window_sum // window_len

        if numbers[right_index] > average:
            window_sum -= numbers[left_index]
            left_index += 1

        window_len = right_index - left_index + 1
        if window_len > answer_frequency:
            answer_frequency = window_len
            answer_number = numbers[right_index]

    print(answer_frequency, answer_number)
        

if __name__ == "__main__":
    main()
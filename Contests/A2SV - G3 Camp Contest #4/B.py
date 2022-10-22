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

    for right_index in range(1, length):
        window_len = right_index - left_index + 1
        diff = numbers[right_index] - numbers[right_index - 1]
        need = (window_len - 1) * diff
        k -= need

        # Update the window, make it valid
        while k < 0:
            k += numbers[right_index] - numbers[left_index]
            left_index += 1

        # If window is valid
        window_len = right_index - left_index + 1
        if window_len > answer_frequency:
            answer_frequency = window_len
            answer_number = numbers[right_index]

    print(answer_frequency, answer_number)
        

if __name__ == "__main__":
    main()
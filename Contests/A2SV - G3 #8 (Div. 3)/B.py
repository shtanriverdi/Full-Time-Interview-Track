import sys
from collections import defaultdict
input = sys.stdin.readline

def main():

    seven_map = defaultdict(list)
    for i in range(7, 1000, 7):
        digits_cnt = len(str(i))
        seven_map[digits_cnt].append(str(i))

    t = int(input())
    
    for _ in range(t):
        letters = [ *input().strip() ]

        min_answer = 10
        min_number = ""

        digits_cnt = len(letters)
        for possible in seven_map[digits_cnt]:

            diff_digit_count = 0
            for i in range(digits_cnt):
                if letters[i] != possible[i]:
                    diff_digit_count += 1

            if diff_digit_count < min_answer:
                min_answer = diff_digit_count
                min_number = possible

        print("".join(min_number))


if __name__ == "__main__":
    main()
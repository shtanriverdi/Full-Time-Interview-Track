import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    digits = [ *input().strip() ]

    minimum_num = []
    for index, digit in enumerate(digits):
        converted = 9 - int(digit)
        if converted < int(digit):
            minimum_num.append(converted)
        else:
            minimum_num.append(digit)

    if minimum_num[0] == 0:
        minimum_num[0] = digits[0]

    for digit in minimum_num:
        print(digit, end="")
        

if __name__ == "__main__":
    main()
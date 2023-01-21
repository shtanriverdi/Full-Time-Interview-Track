import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        temp = int(input())
        binary = list( input().lstrip('0').strip() )
        n = len(binary)

        if n == 0:
            print("0")
            continue

        zipped = [ binary[0] ]
        for i in range(1, n):
            if zipped[-1] != binary[i]:
                zipped.append( binary[i] )

        has_one = False
        has_zero = False

        answer = 0
        zip_n = len(zipped)
        for i in range(zip_n - 1, -1, -1):
            if zipped[i] == '1':
                has_one = True
                answer += has_zero
            if zipped[i] == '0':
                has_zero = True
                answer += has_one

        print(answer)


if __name__ == "__main__":
    main()

import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):

        n = int(input())
        word = [ *input().strip() ]
        un_a = []
        un_b = []

        # Left to right
        chars_set_a = set()
        chars_set_b = set()
        for i in range(n):
            letter_a = word[i]
            chars_set_a.add( letter_a )
            un_a.append(len(chars_set_a))
            
            letter_b = word[n - i - 1]
            chars_set_b.add( letter_b )
            un_b.append(len(chars_set_b))

        un_b.reverse()
        un_b.append( 0 )
        answer = 0
        for i in range(n):
            answer = max(answer, (un_a[i] + un_b[i + 1]))

        print(answer)


if __name__ == "__main__":
    main()

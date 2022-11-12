import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        letters = [ *input().strip() ]
        
        answer = [-1, -1]
        for i in range(1, n):
            if letters[i] != letters[i - 1]:
                answer = [i, i + 1]
                break                

        print(answer[0], answer[1])
        

if __name__ == "__main__":
    main()
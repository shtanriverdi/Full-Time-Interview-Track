import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    n, s = list(map(int, input().split()))
    s -= 1

    R = input().split()
    L = input().split()

    if R[0] == '0':
        print("NO")
        sys.exit(0)

    if R[s] == '1':
        print("YES")
        sys.exit(0)

    if L[s] == '0':
        print("NO")
        sys.exit(0)

    answer = "NO"
    for i in range(s + 1, n):
        if R[i] == '1' and L[i] == '1':
            answer = "YES"
            break

    print(answer)

if __name__ == "__main__":
    main()
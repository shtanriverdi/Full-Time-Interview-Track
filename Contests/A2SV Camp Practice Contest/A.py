import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(index, planes, uniqs, A, recursion_count):
    if len(uniqs) > 3 or recursion_count > 3:
        return False

    if len(uniqs) == 3 and planes[index] == A:
        return True

    uniqs.add(planes[index])

    return dfs(planes[index] - 1, planes, uniqs, A, recursion_count + 1)

def main():
    n = int(input())
    planes = list(map(int, input().split()))

    answer = "NO"
    i = 0
    for plane in planes:
        uniqs = set()

        hasFound = dfs(i, planes, uniqs, planes[i], 0)
        if hasFound:
            answer = "YES"
            break

        i += 1

    print(answer)
        

if __name__ == "__main__":
    main()
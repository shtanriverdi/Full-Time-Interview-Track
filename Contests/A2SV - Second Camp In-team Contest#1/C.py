import sys
input = sys.stdin.readline

def main():
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    nums.sort()

    uniqs = set()
    for num in nums:
        if num not in uniqs:
            uniqs.add(num * k)

    print(len(uniqs))

if __name__ == "__main__":
    main()

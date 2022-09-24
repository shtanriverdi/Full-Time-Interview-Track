import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        nums.reverse()

        uniqs = set()
        for num in nums:
            if num not in uniqs:
                uniqs.add(num)
            else:
                break

        print(n - len(uniqs))

if __name__ == "__main__":
    main()
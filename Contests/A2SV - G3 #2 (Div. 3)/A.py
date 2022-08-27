import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        num_set = set()

        for num in nums:
            if num in num_set:
                num += 1
            num_set.add(num)

        print(len(num_set))

if __name__ == "__main__":
    main()
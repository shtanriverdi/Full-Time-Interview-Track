import sys
input = sys.stdin.readline

def main():
    n = int(input())
    nums = list(map(int, input().split()))

    total_cost = 0
    has_zero = False
    has_negative = False

    for num in nums:
        if num < 0:
            total_cost += abs(num) - 1
            has_negative = not has_negative
        else:
            total_cost += abs(num - 1)
            if num == 0:
                has_zero = True
            
    if has_negative and has_zero == False:
        total_cost += 2 

    print(total_cost)


if __name__ == "__main__":
    main()
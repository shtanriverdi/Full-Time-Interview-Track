import sys
input = sys.stdin.readline

def main():
    n = int(input())
    nums = list(map(int, input().split()))

    max_result = nums[0]
    for i in range(len(nums)):
        cur_xor = nums[i]
        max_result = max(cur_xor, max_result)
        for j in range(i + 1, len(nums)):
            cur_xor ^= nums[j]
            max_result = max(cur_xor, max_result)
    
    print(max_result)

if __name__ == "__main__":
    main()
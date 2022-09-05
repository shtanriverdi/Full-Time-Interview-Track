import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))

        even_count = 0
        odd_count = 0
        for num in nums:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        if even_count == 0 or odd_count == 0:
            print("YES")
            
        # Check if it is alternating
        else:
            is_alternating = True
            for i in range(1, n):
                prev = (nums[i - 1] % 2)
                current = (nums[i] % 2)
                if prev == current:
                    is_alternating = False
                    break

            if is_alternating:
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    main()
import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):

        n, q = list(map(int, input().split()))

        # Process the numbers
        nums = list(map(int, input().split()))
        odd_sum = 0
        odd_cnt = 0
        even_sum = 0
        even_cnt = 0
        for num in nums:
            # Even
            if num % 2 == 0:
                even_sum += num
                even_cnt += 1
            # Odd
            else:
                odd_sum += num
                odd_cnt += 1
                
        # Process the queries
        for _ in range(q):
            q_type, add = list(map(int, input().split()))
            # ODDS
            if q_type == 1:
                odd_sum += (odd_cnt * add)
                if add % 2 == 1:
                    even_cnt += odd_cnt
                    odd_cnt = 0
                    even_sum += odd_sum
                    odd_sum = 0

            # EVENS
            else:
                even_sum += (even_cnt * add)
                if add % 2 == 1:
                    odd_cnt += even_cnt
                    even_cnt = 0
                    odd_sum += even_sum
                    even_sum = 0
                    
            print(odd_sum + even_sum)

if __name__ == "__main__":
    main()
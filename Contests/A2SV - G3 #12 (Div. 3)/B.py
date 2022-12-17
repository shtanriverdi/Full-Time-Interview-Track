import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):

        size = int(input())
        nums = list(map(int, input().split()))
        answer = [0]*size

        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > 2:
                heapq.heappop(min_heap)

        second_max = heapq.heappop(min_heap)
        first_max = heapq.heappop(min_heap)

        for i, num in enumerate(nums):
            if num == first_max:
                answer[i] = num - second_max
            else:
                answer[i] = num - first_max

        for ans in answer:
            print(ans, end=" ")
        print("")

if __name__ == "__main__":
    main()
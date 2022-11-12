import sys
import heapq
from collections import defaultdict
from collections import Counter
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        digits = list(map(int, input().split()))
        
        answer = 0
        counts = Counter(digits)
        max_heap = []
        for digit, count in counts.items():
            if count == 1:
                answer += 1
            else:
               heapq.heappush(max_heap, -count)
        
        while len(max_heap) >= 2:
            first_count  = heapq.heappop(max_heap)
            first_count *= -1
            second_count  = heapq.heappop(max_heap)
            second_count *= -1

            decrease_amount = second_count - 1
            first_count -= decrease_amount
            second_count -= decrease_amount

            if first_count == 1:
                answer += 1
            else:
                heapq.heappush(max_heap, -first_count)

            if second_count == 1:
                answer += 1
            else:
                heapq.heappush(max_heap, -second_count)

        # Process last element
        if len(max_heap) > 0:
            last_count = max_heap[0]
            if last_count % 2 == 1:
                answer += 1

        print(answer)


if __name__ == "__main__":
    main()
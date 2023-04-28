import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
          
        while len(max_heap) > 1:
            A = -heapq.heappop(max_heap)
            B = -heapq.heappop(max_heap)
            newStone = A - B
            if newStone > 0:
                heapq.heappush(max_heap, -newStone)
        
        return 0 if (len(max_heap) == 0) else (-heapq.heappop(max_heap))
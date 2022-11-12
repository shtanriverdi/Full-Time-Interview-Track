class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        max_heap_len = len(self.max_heap)
        min_heap_len = len(self.min_heap)
        diff = max_heap_len - min_heap_len
        
        if diff == 2:
            popped = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -popped)
        elif diff == 1 and min_heap_len > 0 and -self.max_heap[0] > self.min_heap[0]:
            max_popped = heapq.heappop(self.max_heap)
            min_popped = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_popped)
            heapq.heappush(self.min_heap, -max_popped)
            
    def findMedian(self) -> float:
        max_heap_len = len(self.max_heap)
        min_heap_len = len(self.min_heap)
        median = -self.max_heap[0]
        if min_heap_len == max_heap_len:
            median = (median + self.min_heap[0]) / 2
        return median
                
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
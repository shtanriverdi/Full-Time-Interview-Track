from sortedcontainers import SortedSet
class ExamRoom:
    def __init__(self, n: int):
        self.first_index = 0
        self.last_index = n - 1
        
        # Returns the best interval option for next student to sit, maintains sorted order
        self.interval_set = SortedSet([ (self.first_index, self.last_index) ], key = lambda x: (-self.getDist(x[0], x[1]), x[1]))
        
        # To help finding interval_set in above set, we use indices to map interval_set
        self.interval_map = defaultdict(list)
        self.interval_map[self.first_index] = [self.first_index, self.last_index]
        self.interval_map[self.last_index] = [self.first_index, self.last_index]
        
    def removeFromIntervalMap(self, start, end):
        self.interval_map.pop(start)
        # If map has only one entry like: 1: [1, 1]
        if end in self.interval_map:
            self.interval_map.pop(end)
        
    def addToIntervalMap(self, start, end):
        self.interval_map[start] = [start, end]
        self.interval_map[end] = [start, end]
        
    def seat(self) -> int:
        # Get the best interval for student to sit
        start, end = self.interval_set.pop(0)
        
        # Remove this old entry from interval map
        self.removeFromIntervalMap(start, end)
        
        # Case first_index:
        if start == self.first_index and start != end:
            self.interval_set.add( (self.first_index + 1, end) )
            # Add new entry to interval map
            self.addToIntervalMap(self.first_index + 1, end)
            return self.first_index
        
        # Case last_index:
        if end == self.last_index and start != end:
            self.interval_set.add( (start, self.last_index - 1) )
            # Add new entry to interval map
            self.addToIntervalMap(start, self.last_index - 1)
            return end
        
        # Sit the next god damn student in the middle:
        mid = (start + end) // 2
        
        # If [1, 1] etc
        if start == end:
            return mid
        
        if start != mid:
            self.interval_set.add( (start, mid - 1) )
        self.interval_set.add( (mid + 1, end) )
        
        if start != mid:
            self.addToIntervalMap(start, mid - 1)
        self.addToIntervalMap(mid + 1, end)
        
        return mid

    def leave(self, p: int) -> None:
        right_index = p + 1
        left_index = p - 1
        right_interval = None
        if right_index in self.interval_map:
            right_interval = self.interval_map[right_index]
            # Remove this old entry from interval map
            self.removeFromIntervalMap(right_interval[0], right_interval[1])
            # Also remove from interval set
            self.interval_set.discard( (right_interval[0], right_interval[1]) )
            
        left_interval = None
        if left_index in self.interval_map:
            left_interval = self.interval_map[left_index]
            # Remove this old entry from interval map
            self.removeFromIntervalMap(left_interval[0], left_interval[1])
            # Also remove from interval set
            self.interval_set.discard( (left_interval[0], left_interval[1]) )
        
        # If no interval found on both ends
        new_start = p
        new_end = p
        
        # If left interval found
        if left_interval != None:
            new_start = left_interval[0]
            
        # If right interval found
        if right_interval != None:
            new_end = right_interval[1]
        
        self.interval_set.add( (new_start, new_end) )
        self.addToIntervalMap(new_start, new_end)
        
    # Calculate distance score for each interval
    def getDist(self, start, end):
        if start == self.first_index:
            return end + 1
        
        if end == self.last_index:
            return end - start + 1
        
        length = end - start + 1
        mid = (start + end) // 2 + (length % 2 == 0)
        return (end + 1) - mid
        
# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
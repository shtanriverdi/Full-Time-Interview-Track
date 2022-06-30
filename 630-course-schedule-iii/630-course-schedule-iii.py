import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Sort by end days, earlier end day comes first
        courses.sort(key = lambda course: course[1])
        total_days = 0
        max_heap = []
        for duration, last_day in courses:
            total_days += duration
            heappush(max_heap, -duration)
            if total_days > last_day:
                total_days += heappop(max_heap)
        
        return len(max_heap)
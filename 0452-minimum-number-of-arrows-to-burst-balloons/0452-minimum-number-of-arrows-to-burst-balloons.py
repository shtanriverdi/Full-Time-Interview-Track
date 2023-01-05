class Solution:
    def is_overlapping(self, A, B):
        if B[0] <= A[1]:
            return True
        return False
        
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda point: point[1])
        crossings = 1
        n = len(points)
        A = points[0]
        for i in range(1, n):
            B = points[i]
            if self.is_overlapping(A, B) == False:
                crossings += 1
                A = B
            
        return crossings
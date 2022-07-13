class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = [0]*n
        for source, dest in edges:
            indegrees[dest] += 1
            
        result = []
        for node, degree in enumerate(indegrees):
            if degree == 0:
                result.append(node)
                
        return result

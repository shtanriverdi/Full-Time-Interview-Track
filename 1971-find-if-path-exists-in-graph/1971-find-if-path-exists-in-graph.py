class Solution:
    def hasPath(self, current, destination, graph, seen):
        if current == destination:
            return True
        
        seen.add( current )
        pathFound = False
        for neighbour in graph[current]:
            if neighbour not in seen:
                pathFound = self.hasPath(neighbour, destination, graph, seen)
                if pathFound:
                    return True
                
        return pathFound
        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = set()
        hasPath = self.hasPath(source, destination, graph, seen)
        return hasPath
class Solution:
    def helper(self, current, graph, answer, labels, seen):
        seen[current] = True
        count_map = defaultdict(int)
        for neighbour in graph[current]:
            if seen[neighbour] == False:
                neighbor_count_map = self.helper(neighbour, graph, answer, labels, seen)
                for key, value in neighbor_count_map.items():
                    count_map[key] += value
            
        count_map[ labels[current] ] += 1
        answer[ current ] = count_map[ labels[current] ]
        
        return count_map
    
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append( b )
            graph[b].append( a )
            
        answer = [0] * n
        seen = [False] * n
        self.helper(0, graph, answer, labels, seen)
        
        return answer
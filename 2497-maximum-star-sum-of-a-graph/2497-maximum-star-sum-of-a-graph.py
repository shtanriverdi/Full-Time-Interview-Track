import heapq

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        n = len(vals)
        for i in range(n):
            graph[i]
        
        for a, b in edges:
            graph[a].append( b )
            graph[b].append( a )
            
        for node, neighbours in graph.items():
            neighbours.sort(key = lambda node: -vals[node])
        
        answer = vals[0]
        for node, neighbours in graph.items():
            # Have k biggest nodes
            node_sum = vals[node]
            answer = max(answer, node_sum)
            edge_count = 0
            for neighbor in neighbours:
                node_sum += vals[neighbor]
                edge_count += 1
                if edge_count > k:
                    node_sum -= vals[neighbor]
                answer = max(answer, node_sum)
                
        return answer
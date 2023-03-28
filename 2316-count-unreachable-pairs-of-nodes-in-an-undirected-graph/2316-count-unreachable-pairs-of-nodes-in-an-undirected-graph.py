class Solution:
    def dfs(self, cur, graph, seen):
        seen[cur] = True
        nodes = 1
        for neighbor in graph[cur]:
            if seen[neighbor] == False:
                nodes += self.dfs(neighbor, graph, seen)
        return nodes     
        
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [ [] for _ in range(n) ]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False]*n
        answer = 0
        node_sum = 0
        for node in range(n):
            if seen[node] == False:
                count = self.dfs(node, graph, seen)
                answer += (node_sum * count)
                node_sum += count
            
        return answer
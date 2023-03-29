class Solution:
    def dfs(self, cur, seen, graph):
        seen[cur] = True
        node_count = 1
        for neighbor in graph[cur]:
            if seen[neighbor] == False:
                node_count += self.dfs(neighbor, seen, graph)
        return node_count
    
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        graph = [ [] for _ in range(n) ]
        indegrees = [0]*n
        for source, dest in enumerate(edges):
            if dest != -1:
                graph[source].append(dest)
                indegrees[dest] += 1
        
        todo = deque([])
        for node in range(n):
            if indegrees[node] == 0:
                todo.append(node)
        
        while todo:
            cur = todo.popleft()
            for neighbor in graph[cur]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    todo.append(neighbor)
        
        longest_cycle_len = -1
        seen = [False]*n
        for node in range(n):
            if indegrees[node] != 0:
                if seen[node] == False:
                    cur_cycle_len = self.dfs(node, seen, graph)
                    longest_cycle_len = max(longest_cycle_len, cur_cycle_len)
                
        return longest_cycle_len
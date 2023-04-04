class Solution:
    def bfs(self, node, answer, graph):
        seen = set([node])
        todo = deque([node])
        depts = defaultdict(int)
        depts[node] = 0
        parents = defaultdict(int)
        parents[node] = -1
        while todo:
            cur = todo.popleft()
            for neighbor in graph[cur]:
                if neighbor not in seen:
                    todo.append(neighbor)
                    seen.add(neighbor)
                    depts[neighbor] = depts[cur] + 1
                    parents[neighbor] = cur
                elif neighbor != parents[cur]:
                    answer[0] = min(answer[0], depts[neighbor] + depts[cur] + 1)
                
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = [ [] for _ in range(n) ]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        answer = [1001]
        for node in range(n):
            self.bfs(node, answer, graph)
        
        if answer[0] == 1001:
            answer[0] = -1
        
        return answer[0]
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegrees = [0]*n
        for src, dest in edges:
            graph[src].append(dest)
            indegrees[dest] += 1
            
        head_nodes = deque([])
        for node, indegree in enumerate(indegrees):
            if indegree == 0:
                head_nodes.append(node)
        
        # BFS Kahn's Algorithm
        answer = 0
        processed_nodes = 0
        counts = [ [0]*26 for _ in range(n) ]
        while head_nodes:
            cur = head_nodes.popleft()
            counts[cur][ord(colors[cur]) - 97] += 1
            answer = max(answer, max(counts[cur]))
            processed_nodes += 1
            for neighbor in graph[cur]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    head_nodes.append(neighbor)
                for i in range(26):
                    counts[neighbor][i] = max(counts[neighbor][i], counts[cur][i])
                    
        if processed_nodes != n:
            return -1
        
        return answer
class Solution:
    def query(self, start_node, end_node, graph, cache):
        todo = deque([(start_node, 1.0)])
        seen = set([start_node])
        while todo:
            cur_node, cur_cost = todo.popleft()
            # Cache
            cache[(start_node, cur_node)] = cur_cost
            if cur_node == end_node:
                return cur_cost
            # Search the neighbors
            for neighbor, cost in graph[cur_node]:
                if neighbor not in seen:
                    new_cost = cost * cur_cost
                    todo.append( [neighbor, new_cost] )
                    seen.add( neighbor )
        return -1
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        # Contruct the weighted directed graph
        for i, (a, b) in enumerate(equations):
            cost = values[i]
            graph[a].append( [b, cost] )
            graph[b].append( [a, 1 / cost] )
        
        # Get answers for each query
        answers = []
        cache = defaultdict(int)
        for start_node, end_node in queries:
            has_calculted = (start_node, end_node) in cache
            is_valid_nodes = (start_node in graph) and (end_node in graph)
            if has_calculted == False and is_valid_nodes:
                answer = self.query(start_node, end_node, graph, cache)
                answers.append( answer )
            elif has_calculted:
                answers.append( cache[(start_node, end_node)] )
            else:
                answers.append(-1)
        
        return answers
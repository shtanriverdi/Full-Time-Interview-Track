import sys, heapq
input = sys.stdin.readline

def main():
    nodes, edges = list(map(int, input().split()))
    
    graph = {}
    
    neighbors = [ [] for _ in range(nodes + 1) ]
    
    for _ in range(edges):
        ai, bi, wi  = list(map(int, input().split()))
        neighbors[ai].append(bi)
        neighbors[bi].append(ai)
        if (ai, bi) not in graph or wi < graph[(ai, bi)]:
            graph[(ai, bi)] = wi
        if (bi, ai) not in graph or wi < graph[(bi, ai)]:
            graph[(bi, ai)] = wi

    found = False
    min_heap = []
    heapq.heappush(min_heap, (0, 1))
    
    parent_list = [-1]*(nodes + 1)
    min_cost_list = [float("inf")]*(nodes + 1)
    seen = [False]*(nodes + 1)
    
    min_cost_list[1] = 0
    
    while min_heap:
        total_cost, cur_node = heapq.heappop(min_heap)
        seen[cur_node] = True
        
        if cur_node == nodes:
            found = True
            break
        
        for neighbor in neighbors[cur_node]:
            neighbor_cost = graph[(cur_node, neighbor)]
            
            new_cost = neighbor_cost + total_cost
            prev_cost = min_cost_list[neighbor]
            
            if seen[neighbor] == False and new_cost < prev_cost:
                heapq.heappush(min_heap, (new_cost, neighbor))
                parent_list[neighbor] = cur_node
                min_cost_list[neighbor] = new_cost
    
    if found:
        cur_parent = parent_list[nodes]
        result = [ nodes, cur_parent ]
        
        while cur_parent != 1:
            cur_parent = parent_list[cur_parent]
            result.append(cur_parent)
            
        for i in reversed(range(len(result))):
            print(result[i])
    else:
        print("-1")
    

if __name__ == "__main__":
    main()
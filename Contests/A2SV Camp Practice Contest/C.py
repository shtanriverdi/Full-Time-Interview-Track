import sys
from collections import defaultdict
input = sys.stdin.readline

def isRing(graph):
    for current_node, edges in graph.items():
        if len(edges) != 2:
            return False
    return True

def isBus(graph, n):
    one_edge_count = 0
    two_edge_count = 0
    for current_node, edges in graph.items():
        if len(edges) == 1:
            one_edge_count += 1
        elif len(edges) == 2:
            two_edge_count += 1

    if one_edge_count == 2 and two_edge_count == n - 2:
        return True
    return False

def isStar(graph, n):
    one_edge_count = 0
    max_edges = 0
    for current_node, edges in graph.items():
        if len(edges) == 1:
            one_edge_count += 1
        max_edges = max(max_edges, len(edges))

    if one_edge_count == n - 1 and max_edges == n - 1:
        return True
    return False

def main():
    node_count, edge_count = list(map(int, input().split()))

    graph = defaultdict(list)
    for _ in range(edge_count):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)

    if isRing(graph):
        print("ring topology")

    elif isBus(graph, node_count):
        print("bus topology")

    elif isStar(graph, node_count):
        print("star topology")

    else:
        print("unknown topology")
        

if __name__ == "__main__":
    main()
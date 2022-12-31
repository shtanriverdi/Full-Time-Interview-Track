import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs(start_node, graph, mode):
    seen = set()
    seen.add(start_node)

    furthest_node = -1
    furthest_node_distance = -1

    todo = deque()
    todo.append( [start_node, 0] )
    while todo:
        cur_node, parent_distance = todo.popleft()
        for neighbor in graph[cur_node]:
            if neighbor not in seen:
                new_distance = parent_distance + 1
                todo.append( [neighbor, new_distance] )
                seen.add( neighbor )
                if new_distance > furthest_node_distance:
                    furthest_node_distance = new_distance
                    furthest_node = neighbor

    if mode == 0:
        return furthest_node
    return furthest_node_distance

def main():
    node_count, edge_count = list(map(int, input().split()))

    graph = defaultdict(list)
    for _ in range(edge_count):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)

    # First BFS
    far_node = bfs(1, graph, 0)
    # Second BFS
    furhest_node = bfs(far_node, graph, 1453)
    print(furhest_node)

if __name__ == "__main__":
    main()

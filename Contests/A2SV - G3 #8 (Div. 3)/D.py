import sys
from collections import defaultdict, deque

def bfs(start_node, graph, seen):
    todo = deque()
    todo.append(start_node)
    seen.add(start_node)
    valid = True
    while todo:
        cur_node = todo.popleft()
        
        cur_node_edge_count = len(graph[cur_node])
        if cur_node_edge_count != 2:
            valid = False

        for neighbor in graph[cur_node]:
            if neighbor not in seen:
                seen.add(neighbor)
                todo.append(neighbor)

    return valid


def main():
    node_count, edge_count = list(map(int, input().split()))

    graph = defaultdict(list)
    seen = set()

    for _ in range(edge_count):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)

    answer = 0
    for cur_node in range(1, node_count + 1):
        if cur_node not in seen:
            count = bfs(cur_node, graph, seen)
            answer += count

    print(answer)


if __name__ == "__main__":
    main()
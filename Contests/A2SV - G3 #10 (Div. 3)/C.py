import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs(start_node, graph, answer, node_count):
    todo = deque()
    todo.append(start_node)

    seen = set()
    seen.add(start_node)

    number_of_processed_nodes = 1
    while todo:
        cur_node = todo.popleft()

        # Update each node's news count
        answer[cur_node - 1] = node_count

        for neighbor in graph[cur_node]:
            if neighbor not in seen:
                seen.add(neighbor)
                todo.append(neighbor)
                number_of_processed_nodes += 1

    return number_of_processed_nodes

def main():
    node_count, group_count = list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(group_count):
        nodes_in_group = list(map(int, input().split()))
        k = nodes_in_group[0]
        for ith in range(2, len(nodes_in_group)):
            node_A = nodes_in_group[ith]
            node_B = nodes_in_group[ith - 1]
            graph[node_A].append(node_B)
            graph[node_B].append(node_A)

    answer = [-1] * node_count
    for ith_node in range(1, node_count + 1):
        if answer[ith_node - 1] == -1:
            # Count total nodes in the group
            node_count = bfs(ith_node, graph, answer, -1)
            # Update news count for each node in the group
            bfs(ith_node, graph, answer, node_count)
            
    for ans in answer:
        print(ans,end=" ")

if __name__ == "__main__":
    main()
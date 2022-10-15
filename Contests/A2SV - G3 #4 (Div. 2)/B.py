import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def main():
    t = int(input())

    for _ in range(t):
        new_line = input()

        total_nodes, k = list(map(int, input().split()))
        
        # 1 Node case
        if total_nodes == 1:
            print("0")
            continue

        graph = defaultdict(list)
        edge_count = defaultdict(int)

        for _ in range(total_nodes - 1):
            a, b = list(map(int, input().split()))
            graph[b].append(a)
            graph[a].append(b)
            edge_count[a] += 1
            edge_count[b] += 1

        todo = deque()
        for node, count in edge_count.items():
            if count == 1:
                todo.append(node)

        processed_nodes = 0

        while todo:

            if processed_nodes == total_nodes or k == 0:
                break

            level_nodes_len = len(todo)
            while level_nodes_len and k > 0:

                current_node = todo.popleft()
                processed_nodes += 1

                for neigh in graph[current_node]:
                    edge_count[neigh] -= 1
                    if edge_count[neigh] == 1:
                        todo.append(neigh)

                level_nodes_len -= 1

            k -= 1

        print(total_nodes - processed_nodes)

if __name__ == "__main__":
    main()
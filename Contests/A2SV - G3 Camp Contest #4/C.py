# Submit this code by using only "Python 3.8" not PyPy
import sys, threading
from collections import defaultdict

def dfs(current_node, parent_node, graph, consec_cat_count, k, cats, answer, seen):

    seen[current_node] = 1

    if cats[current_node] == 1 and cats[parent_node] == 1:
        consec_cat_count += 1
    else:
        if cats[current_node] == 1:
            consec_cat_count = 1
        else:
            consec_cat_count = 0

    if consec_cat_count > k:
        return

    if len(graph[current_node]) == 1 and current_node != 1:
        if consec_cat_count <= k:
            answer[0] += 1
        return

    for neighbour in graph[current_node]:
        if seen[neighbour] == -1:
            dfs(neighbour, current_node, graph, consec_cat_count, k, cats, answer, seen)

def main():
    nodes_count, k = list(map(int, input().split()))
    cats = [0] + list(map(int, input().split()))

    # Undirected tree rooted at 1
    graph = defaultdict(list)
    for _ in range(nodes_count - 1):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)

    answer = [0]
    consec_cat_count = cats[1]

    seen = [ -1 ] * (nodes_count + 1)
    
    dfs(1, 0, graph, consec_cat_count, k, cats, answer, seen)

    print(answer[0])
        

if __name__ == "__main__":
    threading.stack_size(1 << 27)
    sys.setrecursionlimit(1 << 30)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
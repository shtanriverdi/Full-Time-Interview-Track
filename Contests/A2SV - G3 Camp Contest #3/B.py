from collections import defaultdict, deque
import sys
import heapq
input = sys.stdin.readline

def bfs(start, graph, seen):
    todo = deque([start])
    seen.add(start)
    while todo:
        current = todo.popleft()
        for neigh in graph[current]:
            if neigh not in seen:
                todo.append(neigh)
                seen.add(neigh)
                
def main():
    n, m = list(map(int, input().split()))

    costs = list(map(int, input().split()))

    graph = defaultdict(list)
    for _ in range(m):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)

    min_todo = []
    for ith, cost in enumerate(costs):
        heapq.heappush(min_todo, (cost, ith + 1))

    seen = set()
    answer = 0
    while min_todo:
        cost, node = heapq.heappop(min_todo)
        if node not in seen:
            answer += cost
            bfs(node, graph, seen)

    print(answer)


if __name__ == "__main__":
    main()
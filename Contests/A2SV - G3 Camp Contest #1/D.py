import sys
from collections import defaultdict 
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(current_employee, graph, seen):
    seen[current_employee] = True
    for child in graph[current_employee]:
        if seen[child] == False:
            dfs(child, graph, seen)

def main():
    n, m = list(map(int, input().split()))

    number_of_individuals = 0

    # Build Graph
    graph = defaultdict(list)
    seen = defaultdict(bool)
    for employee_index in range(n):
        langs = list(map(int, input().split()))
        k = langs[0]
        
        # If there is no language
        if k == 0:
            graph[employee_index + 1] = []
            seen[employee_index + 1] = True
            number_of_individuals += 1
        else:
            for ith_lang in range(1, k + 1):
                current_lang = langs[ith_lang] + 100
                graph[current_lang].append(employee_index + 1)
                graph[employee_index + 1].append(current_lang)
                seen[current_lang] = False
                seen[employee_index + 1] = False

    # Run DFS from each Root and find max depth
    number_of_independent_components = 0
    for current_employee in range(1, n + 1):
        if seen[current_employee] == False:
            dfs(current_employee, graph, seen)
            number_of_independent_components += 1

    if number_of_independent_components != 0:
        number_of_independent_components -= 1
    
    print(number_of_independent_components + number_of_individuals)
        

if __name__ == "__main__":
    main()
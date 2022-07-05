class Solution:
    def dfs(self, cur, graph, seen):
        seen.add(cur)
        answer = 1
        for neighbor in graph[cur]:
            if neighbor not in seen:
                answer += self.dfs(neighbor, graph, seen)
        return answer
    
    def longestConsecutive(self, nums: List[int]) -> int:
        graph = {}
        seen = set()
        for num in nums:
            graph[num] = []
            
            prev = num - 1
            Next = num + 1
            if prev in graph:
                graph[prev].append(num)
                graph[num].append(prev)
                
            if Next in graph:
                graph[Next].append(num)
                graph[num].append(Next)
        
        answer = 0
        for num in nums:
            if num not in seen:
                possible_answer = self.dfs(num, graph, seen)
                answer = max(possible_answer, answer)
        
        return answer
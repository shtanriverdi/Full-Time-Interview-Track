class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        task_counts = Counter(tasks)
        answer = 0
        
        for count in task_counts.values():
            if count == 1:
                answer = -1
                break
            times = count // 3
            additional = 1 if (count % 3) > 0 else 0
            answer += times + additional
            
        return answer
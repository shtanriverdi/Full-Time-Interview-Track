class Solution:
    def findAnswerForAGroup(self, start, colors, cost, n):
        cur_index = start
        group_sum = cost[start - 1]
        group_max_val = cost[start - 1]
        while cur_index < n and colors[cur_index - 1] == colors[cur_index]:
            group_max_val = max(group_max_val, cost[cur_index])
            group_sum += cost[cur_index]
            cur_index += 1
        
        group_answer = group_sum - group_max_val
        return [cur_index, group_answer]
    
    def minCost(self, colors: str, costs: List[int]) -> int:
        n = len(colors)
        cur_index = 1
        answer = 0
        while cur_index < n:
            new_index, group_answer = self.findAnswerForAGroup(cur_index, colors, costs, n)
            # print("cur_index:", cur_index, "new_index:",new_index, "group_answer:",group_answer)
            cur_index = new_index + 1
            answer += group_answer
        
        return answer
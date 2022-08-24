class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        memo = [-1] * length
        
        step_1 = self.minCostHelper(0, cost, length, memo)
        step_2 = self.minCostHelper(1, cost, length, memo)
        
        return min(step_1, step_2)
        
    def minCostHelper(self, current_index, cost, length, memo):
        if current_index >= length:
            return 0
        
        if memo[current_index] != -1:
            return memo[current_index]
        
        step_1 = self.minCostHelper(current_index + 1, cost, length, memo)
        step_2 = self.minCostHelper(current_index + 2, cost, length, memo)
        
        memo[current_index] = min(step_1, step_2) + cost[current_index]
        
        return memo[current_index]
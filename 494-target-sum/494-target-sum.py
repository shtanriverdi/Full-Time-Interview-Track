class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)
        memo = [ [-1]*1001 for _ in range(20) ]
        answer = self.helper(0, nums, 0, target, length, memo)
        return answer
    
    def helper(self, current_index, nums, current_sum, target, length, memo):
        if current_index == length:
            if current_sum == target:
                return 1
            return 0
        
        if memo[current_index][current_sum] != -1:
            return memo[current_index][current_sum]
        
        go_positive = self.helper(current_index + 1, nums, current_sum + nums[current_index], target, length, memo)
        go_negative = self.helper(current_index + 1, nums, current_sum - nums[current_index], target, length, memo)
        
        answer = go_positive + go_negative
        memo[current_index][current_sum] = answer
        
        return answer
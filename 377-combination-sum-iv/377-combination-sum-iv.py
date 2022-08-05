class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        size = len(nums)
        memo = [ [-1]*1001 for i in range(size) ]
        return self.helper(0, 0, target, nums, size, memo)
    
    def helper(self, index, current_sum, target, nums, size, memo):
        if current_sum > target:
            return 0
        
        if memo[index][current_sum] != -1:
            return memo[index][current_sum]
        
        if current_sum == target:
            return 1
        
        answer = 0
        for i in range(size):
            answer += self.helper(i, current_sum + nums[i], target, nums, size, memo)
        
        memo[index][current_sum] = answer
        return answer
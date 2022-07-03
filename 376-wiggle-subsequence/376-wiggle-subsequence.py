class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * 1001
        
        return self.helper(0, nums, n, memo, 0)
        
    def helper(self, current_index, nums, n, memo, prev_diff):
        if memo[current_index] != -1:
            return memo[current_index]
        
        result = 1
        for i in range(current_index + 1, n):
            if nums[i] != nums[current_index]:
                curr_diff = 1 if ((nums[i] - nums[current_index]) > 0) else -1
                if curr_diff != prev_diff:
                    one_of_the_answers = self.helper(i, nums, n, memo, curr_diff)
                    result = max(result, 1 + one_of_the_answers)
        
        memo[current_index] = result
        return result
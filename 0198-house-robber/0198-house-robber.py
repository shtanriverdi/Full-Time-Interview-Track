class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.extend( [0, 0] )
        length = len(nums)
        
        for i in range(2, length):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
            nums[i - 1] = max(nums[i - 2], nums[i - 1])
            
        return nums[-1]
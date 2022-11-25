class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        current_sum = sum(nums)
        actual_sum = (n * (n + 1)) // 2
        return actual_sum - current_sum
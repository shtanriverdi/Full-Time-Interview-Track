class Solution:
    def getDifference(self, index, nums, n, pivot_value):
        total_diff = 0
        for i in range(n):
            if i != index:
                total_diff += abs(nums[i] - pivot_value)
        return total_diff
    
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        answer = 0
        index_1, pivot_value_1 = n // 2, nums[n // 2]
        if n % 2 == 0:
            a = self.getDifference(index_1, nums, n, pivot_value_1)
            index_2, pivot_value_2 = (n // 2) - 1, nums[(n // 2) - 1]
            b = self.getDifference(index_2, nums, n, pivot_value_2)
            answer = min(a, b)
        else:
            answer = self.getDifference(index_1, nums, n, pivot_value_1)
        
        return answer
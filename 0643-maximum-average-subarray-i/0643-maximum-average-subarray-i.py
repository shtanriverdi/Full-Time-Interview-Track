class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        running_sum = 0
        answer = float("-inf")
        for i, num in enumerate(nums):
            running_sum += num
            if i + 1 >= k:
                # Update running_sum
                if i - k >= 0:
                    running_sum -= nums[i - k]
                answer = max(answer, running_sum / k)
            
        return answer
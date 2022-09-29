class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length = len(nums)
        zero_count = -k
        right_index = 0
        left_index = 0
        answer = 0
        for right_index in range(right_index, length):
            if nums[right_index] == 0:
                zero_count += 1
            # If window is invalid
            if zero_count > 0:
                zero_count -= 1 if (nums[left_index] <= 0) else 0
                left_index += 1
            # If window is valid
            else:
                answer = max(answer, right_index - left_index + 1)
            
        return answer
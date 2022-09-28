class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        length = len(nums)
        left_index = 0
        window_sum = k
        avg = 0
        nums.sort()
        answer = 0
        for right_index in range(length):
            window_length = right_index - left_index + 1
            window_sum += nums[right_index]
            avg = window_sum // window_length
            if nums[right_index] > avg:
                window_sum -= nums[left_index]
                left_index += 1
                window_length -= 1
            answer = max(answer, window_length)
        
        return answer
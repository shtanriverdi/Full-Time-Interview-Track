class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remaining_map = defaultdict(list)
        remaining_map[0] = -1
        prefix_sum = 0
        for index, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder in remaining_map:
                window_len = index - remaining_map[remainder]
                if window_len > 1:
                    return True
            else:
                remaining_map[remainder] = index
            
        return False
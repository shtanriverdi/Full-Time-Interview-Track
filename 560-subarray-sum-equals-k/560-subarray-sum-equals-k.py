class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        prefix_sum = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        for num in nums:
            prefix_sum += num
            subarray_sum = prefix_sum - k
            if subarray_sum in prefix_map:
                answer += prefix_map[subarray_sum]
            prefix_map[prefix_sum] += 1
            
        return answer
            
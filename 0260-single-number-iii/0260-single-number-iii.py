class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 2:
            return nums
        
        total_sum = sum(nums)
        
        left_count = defaultdict(int)
        for num in nums:
            left_count[total_sum - num] += 1
            
        answer = []
        for num, count in left_count.items():
            if count == 1:
                answer.append(total_sum - num)
        
        return answer
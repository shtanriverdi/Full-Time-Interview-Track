class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1
        
        missing = -1
        duplicate = -1
        n = len(nums)
        for ith_num in range(1, n + 1):
            if num_count[ith_num] == 2:
                duplicate = ith_num
            if num_count[ith_num] == 0:
                missing = ith_num
                
        return [duplicate, missing]
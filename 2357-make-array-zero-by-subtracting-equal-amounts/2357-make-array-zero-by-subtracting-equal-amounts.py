class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        if 0 in counts:
            counts.pop( 0 )
            
        return len(counts)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        unique_set = set()
        for count in counts.values():
            if count in unique_set:
                return False
            unique_set.add( count )
        
        return True
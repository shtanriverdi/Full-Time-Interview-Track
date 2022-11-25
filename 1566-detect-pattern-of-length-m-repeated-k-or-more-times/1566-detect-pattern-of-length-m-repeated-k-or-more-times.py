class Solution:
    def hasPattern(self, start, end, pattern, arr, m):
        for sub_index in range(start, end + 1, m):
            if arr[sub_index:sub_index + m] != pattern:
                return False
        return True
    
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        window_start = 0
        window_end = m * k - 1
        length = len(arr)
        hasPattern = False
        while window_end < length:
            pattern = arr[window_start:window_start + m]
            hasPattern = self.hasPattern(window_start, window_end, pattern, arr, m)
            if hasPattern:
                break
            window_end += 1
            window_start += 1
        
        return hasPattern
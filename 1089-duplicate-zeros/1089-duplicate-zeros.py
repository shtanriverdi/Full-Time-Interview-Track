class Solution:
    def swapper(self, start_index, arr, size):
        for i in reversed(range(start_index, size - 1)):
            arr[i + 1] = arr[i]
        arr[start_index] = 0
        
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        size = len(arr)
        i = 1
        while i < size:
            if arr[i - 1] == 0:
                self.swapper(i, arr, size)
                i += 1
            i += 1
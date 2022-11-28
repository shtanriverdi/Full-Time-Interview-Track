class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        a_len = len(A)
        b_len = len(B)
        total_len = a_len + b_len
        
        kth = ((a_len + b_len) // 2) + 1
        
        a_idx = 0
        b_idx = 0
        
        half_nums = []
        while kth > 0 and a_idx < a_len and b_idx < b_len:
            if A[a_idx] < B[b_idx]:
                half_nums.append( A[a_idx] )
                a_idx += 1
                kth -= 1
            else:
                half_nums.append( B[b_idx] )
                b_idx += 1
                kth -= 1
        
        while kth > 0 and a_idx < a_len:
            half_nums.append( A[a_idx] )
            a_idx += 1
            kth -= 1
            
        while kth > 0 and b_idx < b_len:
            half_nums.append( B[b_idx] )
            b_idx += 1
            kth -= 1
        
        mid_index = total_len // 2
        median = -1
        if total_len % 2 == 1:
            median = half_nums[mid_index]
        else:
            median = (half_nums[mid_index] + half_nums[mid_index - 1]) / 2
        
        return median
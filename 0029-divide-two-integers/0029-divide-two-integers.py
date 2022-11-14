class Solution:
    def divideHelper(self, A, B):
        if A <= 0 or A < B:
            return 0
        
        B_count = 1
        current_pow_B = B
        
        while (current_pow_B << 1) < A:
            current_pow_B <<= 1
            B_count <<= 1
        
        remaining_A = A - current_pow_B
        return B_count + self.divideHelper(remaining_A, B)
    
    def divide(self, A: int, B: int) -> int:
        is_A_negative = -1 if A < 0 else 1
        is_B_negative = -1 if B < 0 else 1
        
        # Make both numbers positive
        Q = self.divideHelper(A * is_A_negative, B * is_B_negative)
        
        # Preserve the negative sign
        Q = Q * is_A_negative * is_B_negative
        
        if Q < -2**31:
            return -2**31
        
        if Q > 2**31 - 1:
            return 2**31 - 1
            
        return Q
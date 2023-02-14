class Solution:
    def getDigitCount(self, n):
        digit_counts = [0]*10
        while n > 0:
            digit_counts[ (n % 10) ] += 1
            n //= 10
        return digit_counts
            
    def reorderedPowerOf2(self, n: int) -> bool:
        power = 0
        base = 2
        n_digit_count = self.getDigitCount(n)
        while base < 1e9:
            base = 2**power
            pow_digit_count = self.getDigitCount(base)
            if pow_digit_count == n_digit_count:
                return True
            power += 1
        
        return False
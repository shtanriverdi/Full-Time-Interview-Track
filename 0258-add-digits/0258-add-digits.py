class Solution:
    def add(self, num):
        total_sum = 0
        while num > 0:
            total_sum += num % 10
            num //= 10
        return total_sum
    
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = self.add(num)
            
        return num
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)
        for index in reversed(range(n)):
            new_num = digits[index] + carry
            digits[index] = new_num % 10
            carry = new_num // 10
            
        if carry == 1:
            return [1] + digits
            
        return digits
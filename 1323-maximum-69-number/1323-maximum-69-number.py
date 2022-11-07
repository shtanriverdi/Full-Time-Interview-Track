class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = list(str(num))
        for index, digit in enumerate(digits):
            if digit == '6':
                digits[index] = '9'
                break
        
        return "".join(digits)
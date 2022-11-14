class Solution:
    def romanToInt(self, s: str) -> int:
        s = s + 'I'
        
        case_map = {
            'I': {'V', 'X'},
            'X': {'L', 'C'},
            'C': {'D', 'M'}
        }
        
        symbol_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        size = len(s)
        integer_value = 0
        for index in range(size - 2, -1, -1):
            letter = s[index]
            right_letter = s[index + 1]
            letter_value = symbol_map[letter]
            if letter in case_map and right_letter in case_map[letter]:
                integer_value -= letter_value
            else:
                integer_value += letter_value
                
        return integer_value
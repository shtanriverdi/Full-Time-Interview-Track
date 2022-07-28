class Solution:
    def get_letter_count(self, s):
        letter_count = [0] * 26
        for letter in s:
            index = ord(letter) - ord('a')
            letter_count[index] += 1
        return letter_count
    
    def isAnagram(self, s: str, t: str) -> bool:
        
        counts_s = self.get_letter_count(s)
        counts_t = self.get_letter_count(t)
        
        return counts_s == counts_t

        
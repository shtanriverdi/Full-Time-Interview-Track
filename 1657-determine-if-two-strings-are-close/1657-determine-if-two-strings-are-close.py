class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        A_freq = list(Counter(word1).values())
        B_freq = list(Counter(word2).values())
        
        A_char_set = set(Counter(word1).keys())
        B_char_set = set(Counter(word2).keys())
        
        A_freq.sort()
        B_freq.sort()
        
        return A_freq == B_freq and A_char_set == B_char_set

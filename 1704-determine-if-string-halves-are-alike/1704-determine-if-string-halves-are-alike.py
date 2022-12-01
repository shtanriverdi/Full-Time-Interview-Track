class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        length = len(s)      
        vowels_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        a_map = defaultdict(int)
        for i in range(length // 2):
            if s[i] in vowels_set:
                a_map[s[i]] += 1
        
        b_map = defaultdict(int)
        for i in range(length // 2, length):
            if s[i] in vowels_set:
                b_map[s[i]] += 1
        
        return sum(a_map.values()) == sum(b_map.values())
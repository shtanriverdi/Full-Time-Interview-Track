class Solution:
    def hasMatched(self, word, pattern, size):
        match_map = {}
        taken_letters = set()
        for i in range(size):
            letter_word = word[i]
            letter_pattern = pattern[i]
            if letter_word not in match_map:
                match_map[letter_word] = letter_pattern
                if letter_pattern in taken_letters:
                    return False
                taken_letters.add(letter_pattern)
            else:
                prev_mapped_letter = match_map[letter_word]
                if prev_mapped_letter != letter_pattern:
                    return False
                
        return True
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        matches = []
        size = len(pattern)
        for word in words:
            match_found = self.hasMatched(word, pattern, size)
            if match_found:
                matches.append(word)
                
        return matches
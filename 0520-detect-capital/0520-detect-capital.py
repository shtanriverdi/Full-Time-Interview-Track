class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital_count = 0
        for letter in word:
            if letter.isupper():
                capital_count += 1
                
        size = len(word)
        if capital_count == size or capital_count == 0 or (capital_count == 1 and word[0].isupper()):
            return True
        return False
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        summary_map = [0] * 26
        for word in words2:
            counts = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                counts[index] += 1
                if counts[index] > summary_map[index]:
                    summary_map[index] = counts[index]
        
        universals = []
        for word in words1:
            universal_found = True
            counts = Counter(word)
            for index, frequency in enumerate(summary_map):
                letter = chr(index + ord('a'))
                if frequency > 0 and (letter not in counts or counts[letter] < frequency):
                    universal_found = False
                    break
            if universal_found:
                universals.append(word)
            
        return universals
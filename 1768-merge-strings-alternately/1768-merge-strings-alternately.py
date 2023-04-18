class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        
        ptrA, lengthA = 0, len(word1)
        ptrB, lengthB = 0, len(word2)
        
        while ptrA < lengthA or ptrB < lengthB:
            if ptrA < lengthA:
                merged.append(word1[ptrA])
                ptrA += 1
            if ptrB < lengthB:
                merged.append(word2[ptrB])
                ptrB += 1
            
        return "".join(merged)
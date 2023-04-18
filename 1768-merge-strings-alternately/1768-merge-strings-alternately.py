class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        
        ptrA, lengthA = 0, len(word1)
        ptrB, lengthB = 0, len(word2)
        turn = True
        
        while ptrA < lengthA or ptrB < lengthB:
            if ptrA < lengthA and turn:
                merged.append(word1[ptrA])
                ptrA += 1
            if ptrB < lengthB and not turn:
                merged.append(word2[ptrB])
                ptrB += 1
            turn = not turn
            
        return "".join(merged)
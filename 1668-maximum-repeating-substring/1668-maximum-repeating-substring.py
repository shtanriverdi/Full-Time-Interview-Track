class Solution:
    def getLongestRep(self, i, A, B, size_A, size_B):
        j = 0
        rep_times = 0
        while i < size_A and j < size_B and A[i] == B[j]:
            i += 1
            j += 1
            if j == size_B:
                j = 0
                rep_times += 1
                
        return rep_times
    
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_k_rep = 0
        size_A = len(sequence)
        size_B = len(word)
        for index, letter in enumerate(sequence):
            if letter == word[0]:
                rep = self.getLongestRep(index, sequence, word, size_A, size_B)
                max_k_rep = max(max_k_rep, rep)
                
        return max_k_rep
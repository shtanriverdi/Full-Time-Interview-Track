class Solution:
    def similarPairs(self, words: List[str]) -> int:
        size = len(words)
        answer = 0
        for i in range(size):
            for j in range(i + 1, size):
                if set(list(words[i])) == set(list(words[j])):
                    answer += 1
                
        return answer
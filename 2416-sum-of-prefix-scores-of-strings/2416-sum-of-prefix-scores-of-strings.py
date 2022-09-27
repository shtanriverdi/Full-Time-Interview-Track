class TrieNode:
    def __init__(self):
        self.count = 0
        self.kids = [None] * 26

class Solution:
    def insert(self, root, word):
        current = root
        for letter in word:
            index = ord(letter) - ord('a')
            if current.kids[index] == None:
                current.kids[index] = TrieNode()
                current.kids[index].count = 1
            else:
                current.kids[index].count += 1
            current = current.kids[index]
    
    def calculate_score(self, root, word):
        score = 0
        current = root
        for letter in word:
            index = ord(letter) - ord('a')
            score += current.kids[index].count
            current = current.kids[index]
        return score
    
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        
        # Insert all the words into Trie
        for word in words:
            self.insert(root, word)
        
        # Calculate answer for each word
        answer = [0] * len(words)
        for index, word in enumerate(words):
            answer[index] = self.calculate_score(root, word)
        
        return answer
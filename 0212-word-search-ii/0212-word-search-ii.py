class TrieNode:
    def __init__(self):
        self.counts = 0
        self.kids = defaultdict(TrieNode)
        self.is_end_of_word = False

class Solution:
    def insert(self, root, word):
        current = root
        for letter in word:
            if letter not in current.kids:
                current.kids[letter] = TrieNode()
            current = current.kids[letter]
            current.counts += 1
        current.is_end_of_word = True
        
    def remove(self, root, word):
        current = root
        for letter in word:
            current = current.kids[letter]
            current.counts -= 1
    
    def dfs(self, i, j, M, N, cur_trie_node, trie_root, board, directions, word, words_found):
        word.append( board[i][j] )
        
        if cur_trie_node.is_end_of_word == True:
            word_found = "".join(word)
            words_found.append( word_found )
            cur_trie_node.is_end_of_word = False
            self.remove(trie_root, word_found)
        
        prev_letter = board[i][j]
        board[i][j] = '*'
        
        for direction in directions:
            ni = i + direction[0]
            nj = j + direction[1]
            if (ni >= 0 and ni < M and nj >= 0 and nj < N) and board[ni][nj] in cur_trie_node.kids and cur_trie_node.kids[board[ni][nj]].counts > 0:
                self.dfs(ni, nj, M, N, cur_trie_node.kids[board[ni][nj]], trie_root, board, directions, word, words_found)
        
        board[i][j] = prev_letter
        word.pop()
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        M = len(board)
        N = len(board[0])
        
        root = TrieNode()
        for word in words:
            self.insert(root, word)
            
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        words_found = []
        for i in range(M):
            for j in range(N):
                if board[i][j] in root.kids:
                    self.dfs(i, j, M, N, root.kids[board[i][j]], root, board, directions, [], words_found)
                
        return words_found
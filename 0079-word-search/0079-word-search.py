# class TrieNode:
#     def __init__(self):
#         self.kids = defaultdict(TrieNode)
#         self.is_end_of_word = False

class Solution:
    # def insert(self, root, word):
    #     curr = root
    #     for letter in word:
    #         if letter not in curr.kids:
    #             curr.kids[letter] = TrieNode()
    #         curr = curr.kids[letter]
    #     curr.is_end_of_word = True
    
    # def search(self, root, word):
    #     curr = root
    #     for letter in word:
    #         if letter not in curr.kids:
    #             return False
    #         curr = curr.kids[letter]
    #     return curr.is_end_of_word == True
    
    def dfs(self, i, j, M, N, board, directions, word_path, word, word_index, word_len):
        if word_index == word_len - 1 and board[i][j] == word[word_index]:
            return True
            
        if word_index < word_len and board[i][j] == word[word_index]:
            prev_letter = board[i][j]
            word_path.append( board[i][j] )
            board[i][j] = '*'

            for direction in directions:
                ni = i + direction[0]
                nj = j + direction[1]
                if ni >= 0 and ni < M and nj >= 0 and nj < N and board[ni][nj] != '*':
                    hasFound = self.dfs(ni, nj, M, N, board, directions, word_path, word, word_index + 1, word_len)
                    if hasFound:
                        return True

            board[i][j] = prev_letter
            word_path.pop()
            # Add into trie to search pruning
            # For this problem, since there is only one word, we don't need to insert all the words
            # self.insert(trie_root, word_path)
        return False
    
    def exist(self, board: List[List[str]], word_str: str) -> bool:
        M = len(board)
        N = len(board[0])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        word_path = []
        
        # Use tries for optimization
        # trie_root = TrieNode()
        
        # Convert word_Str to list of chars
        word = list(word_str)
        word_len = len(word)
        
        for i in range(M):
            for j in range(N):
                has_word = self.dfs(i, j, M, N, board, directions, word_path, word, 0, word_len)
                if has_word:
                    return True
        
        # These lines will make the solution faster is there are many words to search
        # has_word = self.search(trie_root, word)
        # return has_word
        return False
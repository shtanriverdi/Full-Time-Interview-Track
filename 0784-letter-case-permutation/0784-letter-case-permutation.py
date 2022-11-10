class Solution:
    def dfs(self, cur_index, s_len, s, all_possible_strings):
        if cur_index == s_len:
            all_possible_strings.append("".join(s))
            return
            
        if not s[cur_index].isdigit():
            s[cur_index] = s[cur_index].upper()
            self.dfs(cur_index + 1, s_len, s, all_possible_strings)
            
            s[cur_index] = s[cur_index].lower()
            self.dfs(cur_index + 1, s_len, s, all_possible_strings)
            
        else:
            self.dfs(cur_index + 1, s_len, s, all_possible_strings)
    
    def letterCasePermutation(self, s: str) -> List[str]:
        all_possible_strings = []
        s_len = len(s)
        s = list(s)
        self.dfs(0, s_len, s, all_possible_strings)
        return all_possible_strings
from collections import defaultdict, Counter
class Solution:
    def isWindowValid(self, window_map, t_map):
        for letter, count in t_map.items():
            if letter not in window_map or window_map[letter] < count:
                return False
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        
        if n > m:
            return ""
        
        answer = ""
        answer_len = float("inf")
        
        left_index = 0
        right_index = 0
        
        t_map = Counter(t)
        window_map = defaultdict(int)
        
        while right_index < m:
            window_map[s[right_index]] += 1
            while self.isWindowValid(window_map, t_map):
                # Update answer
                window_len = right_index - left_index + 1
                if window_len < answer_len:
                    answer = s[left_index : right_index + 1]
                    answer_len = window_len
                # Update the map and left pointer
                window_map[s[left_index]] -= 1
                left_index += 1
            right_index += 1
        
        return answer
class Solution:
    def isWindowValid(self, window_map):
        for count in window_map.values():
            if count <= 0:
                return False
        return True
    
    def numberOfSubstrings(self, s: str) -> int:
        length = len(s)
        
        window_map = defaultdict(int)
        window_map['a']
        window_map['b']
        window_map['c']
        
        left_index = 0
        answer = 0
        for right_index in range(length):
            window_map[s[right_index]] += 1
            while self.isWindowValid(window_map):
                answer += length - right_index
                window_map[s[left_index]] -= 1
                left_index += 1
        
        return answer
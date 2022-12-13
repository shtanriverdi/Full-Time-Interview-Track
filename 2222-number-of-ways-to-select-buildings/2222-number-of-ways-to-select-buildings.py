class Solution:
    def numberOfWays(self, s: str) -> int:
        length = len(s)

        num_of_zeros_left = [0] * length
        num_of_ones_left = [0] * length
        for i in range(1, length):
            if s[i - 1] == '0':
                num_of_zeros_left[i] += 1
            elif s[i - 1] == '1':
                num_of_ones_left[i] += 1
            num_of_zeros_left[i] += num_of_zeros_left[i - 1]
            num_of_ones_left[i] += num_of_ones_left[i - 1]
            
        num_of_zeros_right = [0] * length
        num_of_ones_right = [0] * length
        for i in range(length - 2, -1, -1):
            if s[i + 1] == '0':
                num_of_zeros_right[i] += 1
            elif s[i + 1] == '1':
                num_of_ones_right[i] += 1
            num_of_zeros_right[i] += num_of_zeros_right[i + 1]
            num_of_ones_right[i] += num_of_ones_right[i + 1]
            
        answer = 0
        for i in range(length):
            if s[i] == '0':
                answer += num_of_ones_right[i] * num_of_ones_left[i]
            elif s[i] == '1':
                answer += num_of_zeros_right[i] * num_of_zeros_left[i]    
        
        return answer
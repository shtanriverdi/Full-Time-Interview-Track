class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        letter_value_map = defaultdict(int)
        for i, letter in enumerate(chars):
            letter_value_map[letter] = vals[i]
        
        values = []
        for letter in s:
            if letter in letter_value_map:
                values.append( letter_value_map[letter] )
            else:
                values.append( ord(letter) - 96 )
        
        # Kadane's Algo
        answer = 0
        running_sum = 0
        for value in values:
            running_sum += value
            if running_sum <= 0:
                running_sum = 0
            answer = max(answer, running_sum)
            
        return answer
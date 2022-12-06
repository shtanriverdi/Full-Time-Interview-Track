class Solution:
    def frequencySort(self, s: str) -> str:
        letter_counts = Counter(s)
        
        count_letter_list = []
        for letter, count in letter_counts.items():
            count_letter_list.append( [count, letter] )
            
        count_letter_list.sort(reverse=True)
        answer = []
        for letter, count in count_letter_list:
            answer += (letter * count)
        
        return "".join(answer)
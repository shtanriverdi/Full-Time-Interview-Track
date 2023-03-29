class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        mono_dec_stack = []
        answer = [0]*n
        for index, cur_height in enumerate(heights):
            while mono_dec_stack and cur_height > heights[mono_dec_stack[-1]]:
                poppod_index = mono_dec_stack.pop()
                answer[poppod_index] += 1
                if mono_dec_stack:
                    answer[mono_dec_stack[-1]] += 1
            mono_dec_stack.append(index)
        
        count = 1
        for index in range(len(mono_dec_stack) - 1):
            poppod_index = mono_dec_stack[index]
            answer[poppod_index] += count
            
        return answer
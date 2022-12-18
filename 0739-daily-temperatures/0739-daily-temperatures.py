class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_dec_stack = []
        
        for index, temperature in enumerate(temperatures):
            while mono_dec_stack and temperature > temperatures[mono_dec_stack[-1]]:
                popped_index = mono_dec_stack.pop()
                temperatures[popped_index] = index - popped_index
            mono_dec_stack.append( index )
        
        while mono_dec_stack:
            temperatures[mono_dec_stack.pop()] = 0
        
        return temperatures
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for letter in s:
            pop_count = 1
            while stack and stack[-1] == letter:
                pop_count += 1
                stack.pop()
            if pop_count % 2 == 1:
                stack.append(letter)
                
        return "".join(stack)
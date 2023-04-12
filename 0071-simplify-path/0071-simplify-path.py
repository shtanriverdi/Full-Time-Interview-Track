class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for letter in path:
            if letter != '.' and letter != '':
                if letter == '..' and stack and stack[-1] != '/':
                    stack.pop()
                elif letter != '..':
                    stack.append('/' + letter)
        
        if not stack:
            stack.append('/')
            
        return "".join(stack)
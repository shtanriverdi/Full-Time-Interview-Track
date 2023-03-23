class BrowserHistory:
    def __init__(self, homepage: str):
        self.current_index = 0
        self.history = [ homepage ]

    def visit(self, url: str) -> None:
        self.current_index += 1
        if self.isInside(self.current_index):
            k = len(self.history) - self.current_index
            self.history = self.history[:-k]
        self.history.append( url )
        
    def back(self, steps: int) -> str:
        self.getOffset(-steps)
        return self.getCurrentUrl()

    def forward(self, steps: int) -> str:
        self.getOffset(steps)
        return self.getCurrentUrl()
        
    def isInside(self, index):
        return 0 <= index < len(self.history)
    
    def getOffset(self, steps):
        offset = self.current_index + steps
        if offset < 0:
            self.current_index = 0
        elif offset >= len(self.history):
            self.current_index = len(self.history) - 1
        else:
            self.current_index = offset
        
    def getCurrentUrl(self):
        return self.history[self.current_index]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
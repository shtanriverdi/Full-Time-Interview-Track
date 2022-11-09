class StockSpanner:
    def __init__(self):
        self.mono_dec_stack = []

    def next(self, price: int) -> int:
        to_be_pushed = [price, 1]
        while self.mono_dec_stack and price >= self.mono_dec_stack[-1][0]:
            to_be_pushed[1] += self.mono_dec_stack[-1][1]
            self.mono_dec_stack.pop()
            
        self.mono_dec_stack.append(to_be_pushed)
        return self.mono_dec_stack[-1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
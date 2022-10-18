class Solution:
    def count(self, string):
        length = len(string)
        zipped = [ [string[0], 1] ]
        for index in range(1, length):
            current_digit = string[index]
            if current_digit == zipped[-1][0]:
                zipped[-1][1] += 1
            else:
                zipped.append( [current_digit, 1] )
        
        new_string = []
        for digit, count in zipped:
            new_string.append(str(count))
            new_string.append(digit)
        
        return "".join(new_string)
    
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev_string = self.countAndSay(n - 1)        
        return self.count(prev_string)
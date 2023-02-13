class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)
        
        max_len = max(a_len, b_len)
        min_len = min(a_len, b_len)
        
        diff = max_len - min_len
        if min_len == a_len:
            a = diff*"0" + a
        else:
            b = diff*"0" + b
                
        answer = []
        carry = 0
        for i in range(max_len - 1, -1, -1):
            a_dig = int(a[i])
            b_dig = int(b[i])
            res_dig = (a_dig ^ b_dig) ^ carry
            answer.append( str(res_dig) )
            carry = 1 if (a_dig + b_dig + carry > 1) else 0
        
        if carry == 1:
            answer.append( "1" )
            
        return "".join(reversed(answer))
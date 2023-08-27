class Solution:
    def reverse(self, x: int) -> int:
        
        s = str(x)
        
        if s[0] == '-':
            s = s[1:]
            result =  -int(s[::-1])
        
        elif s[0] != '-':
            result =  int(s[::-1])
            
        if int(result) > -2 ** 31 and int(result) < 2 ** 31:
            return result
        else:
            return 0

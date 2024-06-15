class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        draken = ""
        ls = list(range(48, 58))
        sign = 0
        
        if len(s) == 0 or (len(s) == 1 and ord(s[0]) not in ls):
            return 0
        if (s[0] == '-' or s[0] == '+') and ord(s[1]) not in ls:
            return 0
        
        
        if s[0] == '+':
            s = s[1:]
        
        if s[0] == "-":
            sign = 1
            s = s[1:]
            s = s.lstrip('0')
        
        if ord(s[0]) not in ls:
            return 0
        
        for i in s:
            if ord(i) in ls:
                
                draken = draken + i
            else:
                break

        if sign == 0:
            if int(draken) >= 2147483648:
                return 2147483647
            return int(draken)
        else:
            if -int(draken) < -2147483648:
                return -2147483648
            return -int(draken)

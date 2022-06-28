class Solution:
    def romanToInt(self, s: str) -> int:
        s = list(s)
        total = 0
        
        ls = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        for i in range(len(s)-1,-1,-1):
            if 4 * ls[s[i]] < total:
                total = total - ls[s[i]]
                
            else:
                total = total + ls[s[i]]
                
        return total

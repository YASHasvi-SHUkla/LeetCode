class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a = int(a,2)
        b = int(b,2)
        
        total = bin(a + b)
        s = str(total)[2:]
        
        return s
        

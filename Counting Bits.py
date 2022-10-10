
class Solution:
    def countBits(self, n: int) -> List[int]:
        ls = []
        for i in range(n+1):
            b = bin(i)
            c = b[2:].count("1")
            
            ls.append(c)
            
        return ls

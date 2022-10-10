
class Solution:
    def hammingWeight(self, n: int) -> int:
        b = str(bin(n))
        s = b[2:]
                
        return s.count("1")

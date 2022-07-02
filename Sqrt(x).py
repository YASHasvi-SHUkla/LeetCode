class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0:
            return 0
        elif x == 1:
            return 1
        
        else:
            for i in range(2,(x//2)+2):
                if i*i > x:
                    return i-1

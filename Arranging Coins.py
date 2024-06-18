class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return n
            
        step = 0
        
        while n >= 0:
            step = step + 1
            
            n = n - step

        return step - 1

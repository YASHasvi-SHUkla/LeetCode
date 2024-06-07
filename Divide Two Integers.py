class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        dd = abs(dividend)
        dv = abs(divisor)
        
        dracule = 0
        
        while dd >= dv:
            temp = dv
            mul = 1
            while dd >= temp:
                dd = dd - temp
                dracule = dracule + mul
                mul = mul + mul
                temp = temp + temp

            
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            return -dracule
        return min(2147483647, max(-2147483648, dracule))

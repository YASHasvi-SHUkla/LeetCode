class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        x = 0
        y = 0
        for i in num1:
            x = x * 10 + (ord(i) - 48)
        for j in num2:
            y = y * 10 + (ord(j) - 48)
        return str(x * y)
      
      

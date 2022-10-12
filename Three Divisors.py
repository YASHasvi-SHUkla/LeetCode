class Solution:
    def isThree(self, n: int) -> bool:
        c = 0
        for i in range(1,n+1):
            if n%i ==0:
                c = c + 1
        if c ==3:
            return True
        else:
            return False
          
                   
#### Runtime: 60 ms, faster than 59.20% of Python3 online submissions for Three Divisors.
#### Memory Usage: 13.8 MB, less than 94.67% of Python3 online submissions for Three Divisors.

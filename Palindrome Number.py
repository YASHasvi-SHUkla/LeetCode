class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        while(x>=0):
            if list(str(x)) == list(reversed(str(x))):
                return True
            else:
                return False


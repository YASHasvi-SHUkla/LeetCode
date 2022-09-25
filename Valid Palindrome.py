
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  #  converting whole string into lowercase
        draken = []
        
        for i in s:
            if ord(i) >= 97 and ord(i) <= 122 or (ord(i) >= 48 and ord(i) <= 57):
                draken.append(i)

        if draken == draken[::-1]:
            return True
        else:
            return False
                     
            
 ##   alphanumeric means ( a to z ) and ( 0 to 9 )


class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)%2 !=0:   #  for checking if number of bracketrs is even for them to be into pair
            return False
          
        while len(s) > 0:
            
            if "()" in s:
                s = s.replace("()","")
            elif "{}" in s:
                s = s.replace("{}","")
            elif "[]" in s:
                s = s.replace("[]","")
            else:
                return False
        return True

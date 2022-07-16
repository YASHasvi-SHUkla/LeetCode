class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = list(s.split())
        
        new_string = ""
        
        for i in range(len(s)-1,-1,-1):
            
            new_string = new_string + s[i] + " "
            
        new_string = new_string.strip()
        
        return new_string
        

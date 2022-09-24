
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      
        string = ""
        for i in digits:
            string = string + str(i)
            
        s = int(string) + 1
        draken = [int(j) for j in str(s)]
        
        return draken

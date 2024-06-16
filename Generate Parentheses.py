class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        draken = []
        mikey = []
        
        def backtracking(openB, closeB):
            
            if openB == closeB == n: # all bracket used
                mikey.append("".join(draken))
                return
            
            if openB < n:
                draken.append("(")
                backtracking(openB + 1, closeB)
                draken.pop()
                
            if closeB < openB:
                draken.append(")")
                backtracking(openB, closeB + 1)
                draken.pop()
                
        backtracking(0,0)
        return mikey

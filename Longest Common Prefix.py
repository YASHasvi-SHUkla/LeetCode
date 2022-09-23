
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pre = ""
        m = min(strs,key=len)
        for i in range(len(strs)):
            for j in range(0,len(strs)+1):

                if strs[i][j] == m[j]:
                    pre = pre + strs[i][j]
            pre = pre + ","

        d = pre.split(",")
        return d[-2]

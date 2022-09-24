
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        m = min(strs,key=len)
        pre = ""
        p = ""
        if len(strs) == 0:
            return p
        if len(strs) == 1:
            return strs[0]
        if strs.count(strs[0]) == len(strs):
            return strs[0]
        
        for i in range(len(strs)):
            if strs[i] != m:
                for j in range(len(m)):
        
                    if strs[i][j] == m[j]:
                        pre = pre + m[j]
                    else:
                        break
                
                pre = pre + ","
        pre = pre[:-1]
        draken = pre.split(",")
        mm = min(draken,key=len)
        return mm

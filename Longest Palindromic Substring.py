class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ls = []
        m = ""
        for i in range(0, len(s)):
            for j in range(i, len(s) + 1):
                ss = s[i:j]
                if ss == ss[::-1] and len(ss) > len(m):
                    m = ss
                    ls.append(ss)
        return max(ls, key=len)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        s = list(set(nums))
        y = s.sort()
        
        l = len(s)
        
        for i in range(l):
            nums.insert(i,s[i])
            
        return l

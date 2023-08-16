class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        s = 0
        draken = -10000
        
        for i in nums:
            s = s + i
            
            draken = max(draken, s)
                
            if s < 0:
                s = 0
            
        return draken

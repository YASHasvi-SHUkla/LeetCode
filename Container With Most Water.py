class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        draken = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            
            area = (right - left) * min(height[left], height[right])
            draken = max(draken, area)
            
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
                
        return draken

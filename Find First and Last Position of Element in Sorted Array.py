class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        ls = nums[::-1]
        
        if nums.count(target) == 0:
            return [-1,-1]
        
        if nums.count(target) == 1:
            draken = nums.index(target)
            return [draken, draken]
        
        if nums.count(target) >= 2:
            draken = nums.index(target)
            mikey = ls.index(target)
            return [draken, (len(ls) - 1) - mikey]

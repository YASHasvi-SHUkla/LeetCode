
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        ## Approach 1
        
        nums.append(target)
        nums.sort()
        return nums.index(target)
    
    
        ## Approach 2
        
        for j in range(len(nums)):
            
            if nums[j] >= target:
                return j
            
        return len(nums)

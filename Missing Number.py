# BRUTE FORCE SOLUTION

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        l = len(nums)
        
        for i in range(l + 1):
            if i not in nums:
                return i

# USING SET OPERATIONS

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        ls = set(list(range(len(nums) + 1)))
        s = set(nums)
        draken = list(ls -s)
        return draken[0]

# USING SUM FUNCTION

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        return sum(list(range(len(nums) + 1))) - sum(nums)
      

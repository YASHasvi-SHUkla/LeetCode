class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        y = 0
        for i in nums:
            y = y ^ i
        
        return y

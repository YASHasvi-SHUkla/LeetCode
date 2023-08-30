class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashing = set()
        
        for i in nums:
            if i in hashing:
                return True
            hashing.add(i)
        else:
            return False
        

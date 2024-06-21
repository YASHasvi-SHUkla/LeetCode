class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ls = []
        
        for i in nums1:
            if i in nums2:
                ls.append(i)
                
        return list(set(ls))

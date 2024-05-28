class Solution:
    import math
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        arr = nums1 + nums2
        arr.sort()
        
        if len(arr) == 1:
            return arr[0]
        
        if len(arr) % 2 != 0:
            return arr[len(arr) // 2]
        else:
            return (arr[math.floor(len(arr) / 2 - 1)] + arr[math.ceil(len(arr) / 2)])/2
            

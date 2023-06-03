
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for j in range(m,m+n):
            
            nums1[j] = nums2[j-m]
        nums1.sort()

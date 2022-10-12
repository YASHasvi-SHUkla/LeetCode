class Solution:
    def findGCD(self, nums: List[int]) -> int:
        ls = []
        for i in range(1,max(nums)+1):
            if min(nums)%i ==0 and max(nums)%i == 0:
                ls.append(i)
        if len(ls) >0:
            return max(ls)
        else:
            return 1
          

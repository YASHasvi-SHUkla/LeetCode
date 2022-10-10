
class Solution:
    
    def trimMean(self, arr: List[int]) -> float:
        import statistics
        n = 0.05 * len(arr)
        for i in range(int(n)):
        
            arr.remove(min(arr))
            arr.remove(max(arr))
        
        return statistics.mean(arr)

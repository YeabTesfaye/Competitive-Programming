class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first, second  = float('inf'), float('inf')

        for thrid in nums:
            if second < thrid: return True
            
            if thrid <= first:
                first = thrid 
            else:
                second = thrid 
        return False 
        
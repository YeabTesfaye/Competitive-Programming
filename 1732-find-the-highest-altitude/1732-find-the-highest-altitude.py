class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        curSum, maxCur = 0,0

        for i in range(len(gain)):
            curSum += gain[i]
            maxCur = max(maxCur,curSum)
        
        return maxCur
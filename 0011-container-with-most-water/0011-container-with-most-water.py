class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxA = float('-inf')
        rp = len(height) - 1
        lp = 0 
        while lp < rp:
            area = (rp-lp)*min(height[lp], height[rp])
            maxA = max(maxA, area)
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
        return maxA
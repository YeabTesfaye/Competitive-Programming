class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        #O(mlogm + nlogm)
        #sort the potions array

        potions.sort()
        res = []

        for s in spells:
            l = 0
            r = len(potions) - 1
            idx = len(potions) # the furthest potion index 
            
            while l <= r:
                m = (l + r)//2
                if s*potions[m] >= success:
                    r = m - 1
                    idx = m
                else:
                    l = m + 1
            res.append(len(potions) - idx)
        return res
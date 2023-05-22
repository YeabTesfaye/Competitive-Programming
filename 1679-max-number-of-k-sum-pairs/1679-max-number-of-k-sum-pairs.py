class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #two pointer 
        nums.sort()
        lp = 0
        rp = len(nums) - 1
        count = 0

        while lp < rp:
            if (nums[lp] + nums[rp] < k):
                lp += 1
            elif (nums[lp] + nums[rp] > k):
                rp -= 1
            else:
                #we found the pairs so we should go with two sides
                count += 1
                lp += 1
                rp -= 1
        return count

        
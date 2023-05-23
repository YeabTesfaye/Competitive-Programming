class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums: return len(nums) - 1
        left,prev,maxLen = -1,-1,0

        for right in range(len(nums)):
            if nums[right] == 0:
                maxLen = max(maxLen, right-left-2)
                left = prev
                prev = right
        
        if nums[right]: return max(maxLen, right-left-1)
        return max(maxLen, right-left-2)



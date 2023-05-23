class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        sumLeft = 0 
        sumRight = 0

        for i in range(len(nums)):
            sumLeft = sum(nums[:i])
            sumRight = sum(nums[i+1:])

            if sumLeft == sumRight:
                return i
        return -1
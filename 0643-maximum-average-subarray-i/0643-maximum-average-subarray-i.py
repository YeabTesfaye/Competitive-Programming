class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = sum(nums[:k])
        maxAvg = float('-inf')
        maxAvg = max(maxAvg, curSum/k)

        for i in range(k,len(nums)):
            curSum -= nums[i-k]
            curSum += nums[i]
            maxAvg = max(maxAvg, curSum/k)
        return maxAvg
        
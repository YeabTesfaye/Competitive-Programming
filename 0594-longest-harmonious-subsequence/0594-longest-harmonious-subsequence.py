from collections import Counter 
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        freq = Counter(nums)
        max_length = 0

        for num in freq:
            if num + 1 in freq:
                max_length = max(max_length, freq[num] + freq[num + 1])
        return max_length
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                streak = 1

                while current + 1 in nums_set:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest

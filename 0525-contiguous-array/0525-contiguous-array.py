class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Initialize the hashmap to store the first occurrence of prefix sum
        prefix_sum_map = {0:-1}  
        max_length = 0
        prefix_sum = 0

        for i, num in enumerate(nums):
            # Update the prefix sum: treat 0 as -1 and 1 as +1
            prefix_sum += 1 if num == 1 else -1

            # If this prefix sum has been seen before, calculate the length of the subarray
            if prefix_sum in prefix_sum_map:
                # Calculate the length of the subarray
                length = i - prefix_sum_map[prefix_sum]
                max_length = max(max_length, length)
            else:
                prefix_sum_map[prefix_sum] = i

        return max_length

        
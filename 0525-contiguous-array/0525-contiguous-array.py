class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
             # Initialize the hashmap to store the first occurrence of prefix sum
        prefix_sum_map = {0: -1}  # We assume prefix sum 0 occurs at index -1 for subarrays that start from the beginning
        max_length = 0
        prefix_sum = 0

        # Iterate through the array
        for i, num in enumerate(nums):
            # Update the prefix sum: treat 0 as -1 and 1 as +1
            prefix_sum += 1 if num == 1 else -1

            # If this prefix sum has been seen before, calculate the length of the subarray
            if prefix_sum in prefix_sum_map:
                # Calculate the length of the subarray
                length = i - prefix_sum_map[prefix_sum]
                max_length = max(max_length, length)
            else:
                # Store the first occurrence of this prefix sum
                prefix_sum_map[prefix_sum] = i

        return max_length

        
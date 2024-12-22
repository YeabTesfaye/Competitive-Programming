class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Create a hash set to store all possible prefixes of numbers in arr1
        prefix_set = set()
        for x in arr1:
            while x:
                prefix_set.add(x)  
                x //= 10  # Remove the last digit to generate the next prefix

        # Iterate through arr2 to find the longest common prefix with arr1
        longest_prefix_length = 0
        for x in arr2:
            while x:
                if x in prefix_set:
                    # If x is a common prefix, update the longest prefix length
                    longest_prefix_length = max(longest_prefix_length, len(str(x)))
                    break 
                x //= 10 

        return longest_prefix_length

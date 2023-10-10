class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Find the minimum length string in the list.
        min_len = min(len(s) for s in strs)
        
        # Initialize the result as an empty string.
        result = ""

        # Iterate over the characters in the first string (up to the length of the shortest string).
        for i in range(min_len):
            char = strs[0][i]
            print(char)
            # Check if this character is common to all strings.
            if all(s[i] == char for s in strs):
                result += char
            else:
                break

        return result
            
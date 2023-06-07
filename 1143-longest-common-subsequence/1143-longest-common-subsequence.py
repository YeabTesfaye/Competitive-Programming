class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def recursive(idx1,idx2):
            key = (idx1,idx2)

            if key in memo:
                return memo[key]
            elif idx1 == len(text1) or idx2 == len(text2):
                return 0
            elif text1[idx1] == text2[idx2]:
                return 1 + recursive(idx1+1,idx2+1)
            else:
                memo[key] = max(recursive(idx1+1,idx2), recursive(idx1,idx2+1))
            return memo[key]
        return recursive(0,0)
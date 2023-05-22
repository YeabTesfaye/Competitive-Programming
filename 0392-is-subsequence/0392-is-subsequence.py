class Solution:
    def isSubsequence(self, s:str, t:str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True

        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
            if j == len(s):  # All characters in s have been found in t
                return True

        return False  # Some characters in s were not found in t or not in the correct order
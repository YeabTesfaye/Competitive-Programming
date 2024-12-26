class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         
        strSet = set()
        left,right = 0,0
        maxLen = 0

        while right < len(s):
            if s[right] not in strSet:
                strSet.add(s[right])
                maxLen = max(maxLen, (right - left + 1))
                right += 1
            else:
                strSet.remove(s[left])
                left += 1
                # right += 1
        return maxLen

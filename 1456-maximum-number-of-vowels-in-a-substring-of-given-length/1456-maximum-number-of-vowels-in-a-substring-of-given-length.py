class Solution:
    def maxVowels(self,s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        
        l, r, cnt, res = 0, 0, 0, float('-inf')
        
        while l <= r and r < len(s):
            cnt += 1 if s[r] in vowel else 0
            
            if (r - l + 1) > k:
                cnt -= 1 if s[l] in vowel else 0
                l += 1
            r += 1
            res = max(res, cnt)
        
        return res
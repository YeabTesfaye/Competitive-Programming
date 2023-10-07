class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p_count = {}
        for char in p:
            p_count[char] = p_count.get(char,0) + 1

        l,r = 0,0
        count = []
        s_count = {}
        while r < len(s):
            s_count[s[r]] = s_count.get(s[r], 0) + 1

            if (r - l) + 1 == len(p):
                if s_count == p_count:
                    count.append(l)
                s_count[s[l]] -= 1

                if s_count[s[l]] == 0:
                    del s_count[s[l]]
                l += 1
            r += 1
        return count
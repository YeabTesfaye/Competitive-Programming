class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [word for word in s.split() if word]
        if words:
            return len(words[-1])
        return 0
        
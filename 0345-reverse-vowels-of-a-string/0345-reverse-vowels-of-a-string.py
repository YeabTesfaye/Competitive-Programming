class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels= {'a','e','i','o','u'}

        left,right = 0, len(s) - 1
        s = list(s)
        while left < right:
            letftSmall = s[left].lower()
            rightSmall = s[right].lower()

            if letftSmall not in vowels:
                left += 1
                continue 
            if rightSmall not in vowels:
                right -= 1
                continue 
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
        return ''.join(s)


            
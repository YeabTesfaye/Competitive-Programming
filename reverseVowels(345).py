
def reverseVowels(s:str):
    vowels= ['a','e','i','o','u']
    s = list(s) # because of string are immutable we can't directly change it 
    left,right = 0, len(s) - 1

    while right > left:
        rightS = s[right].lower()
        leftS = s[left].lower()

        if leftS not in vowels:
            left += 1
            continue
        if rightS not in vowels:
            right -= 1
            continue
        s[left], s[right] = s[right],s[left]
        left += 1
        right -= 1
    return "".join(s)
   




#Input: s = "leetcode"
s = "leetcode"
print(reverseVowels(s))

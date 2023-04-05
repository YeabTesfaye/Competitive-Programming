def wordBreak(s, wordDict):
    if not s or not wordDict:
        return False
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break
    return dp[0]


#Input: s = "applepenapple", wordDict = ["apple", "pen"]
#Output: true
wordDict = ["apple", "pen"]
s = "applepenapple"
print(wordBreak(s, wordDict))

from itertools import zip_longest

def mergeAlternately(word1:str, word2:str) -> str:
    output = ""
    # Iterate over characters from word1 and word2 simultaneously
    for char1, char2 in zip_longest(word1, word2, fillvalue=''):
        # Merge characters alternately into the output string fillvalue is used 
        #as a default value for charcters with none value
        output += char1 + char2
    return output

# Test cases
word1 = "abcd"  # Input: word1 = "abcd"
word2 = "pq"    # Input: word2 = "pq"
print(mergeAlternately(word1, word2))  # Output: "apbqcd"

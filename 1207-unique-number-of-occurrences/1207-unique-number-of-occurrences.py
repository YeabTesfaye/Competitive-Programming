from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictionary = Counter(arr)
        unique = set()

        for value in dictionary.values():
            unique.add(value)
        return len(unique) == len(dictionary)
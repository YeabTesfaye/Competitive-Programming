class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_splited = s.split(" ")
        mapPT,mapTP ={},{} 
        if len(pattern) != len(s_splited):
            return False
        for c1,c2 in zip(pattern, s_splited):
            
            if (c1 in mapPT and mapPT[c1] != c2) or (c2 in mapTP and mapTP[c2] != c1):
                return False
            mapPT[c1] = c2 
            mapTP[c2] = c1 
        return True
        
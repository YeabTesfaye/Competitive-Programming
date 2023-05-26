class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = []
        rad = []
        l = len(senate)
        for i, v in enumerate(senate):
            if v == "R":
                rad.append(i)
            else:
                dire.append(i)
        
        while len(rad) or len(dire):
            if len(rad) == 0:
                return "Dire"
            if len(dire) == 0:
                return "Radiant"
            if rad[0] < dire[0]:
                rad.append(l)
                l+=1
            else:
                dire.append(l)
                l+=1
            rad.pop(0)
            dire.pop(0)
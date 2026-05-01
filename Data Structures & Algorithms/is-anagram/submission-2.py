class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        if len(s) != len(t):
            return False
        for l in s:
            if l in sDict:
                sDict[l] += 1
            else: 
                sDict[l] = 1
        for l in t:
            if l in tDict:
                tDict[l] += 1
            else: 
                tDict[l] = 1
        for k in sDict:
            if k not in tDict:
                return False
            if sDict[k] != tDict[k]:
                return False
        for k in tDict:
            if k not in sDict:
                return False
            if tDict[k] != sDict[k] or k not in sDict:
                return False
        return True

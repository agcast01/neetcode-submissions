class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = sorted(s)
        sortedT = sorted(t)
        if len(s) != len(t):
            return False

        for x in range(len(s)):
            if sortedS[x] != sortedT[x]:
                return False
        return True
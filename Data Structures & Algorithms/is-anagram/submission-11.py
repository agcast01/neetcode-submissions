class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCountS = {}
        charCountT = {}

        if len(s) != len(t):
            return False
        
        for x in range(len(s)):
            if s[x] in charCountS:
                charCountS[s[x]] += 1
            else:
                charCountS[s[x]] = 1
            if t[x] in charCountT:
                charCountT[t[x]] += 1
            else:
                charCountT[t[x]] = 1

        for y in charCountS:
            if y not in charCountT:
                return False
            if charCountS[y] != charCountT[y]:
                return False
        
        return True
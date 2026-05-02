class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount = {}

        if len(s) != len(t):
            return False
        
        for char in s:
            if char in charCount:
                charCount[char] += 1
            else:
                charCount[char] = 1
        
        for char in t:
            if char in charCount:
                charCount[char] -= 1
            else:
                return False

        for char in charCount:
            if charCount[char] != 0:
                return False
        
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s_lower = s.lower()
        s_filtered = "".join(char for char in s_lower if char in alpha)
        if len(s) == 0:
            return False
        l = 0
        r = len(s_filtered) - 1
        while l < r:
            if s_filtered[l] != s_filtered[r]:
                return False
            l += 1
            r -= 1
        return True
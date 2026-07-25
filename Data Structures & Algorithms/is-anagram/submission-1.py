class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tchars = list(t)
        for char in s:
            if char in tchars:
                tchars.remove(char)
            else:
                return False
        if not tchars:
            return True
        return False
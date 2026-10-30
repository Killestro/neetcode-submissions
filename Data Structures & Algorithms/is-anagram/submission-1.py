class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}
        for si in s: 
            if s.count(si) != t.count(si):
                return False
        return True
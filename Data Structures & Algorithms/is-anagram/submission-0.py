class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}
        for si in s: 
            counter[si] = counter.get(si, 0) + 1
        
        for ti in t: 
            if ti not in counter:
                return False
            counter[ti] = counter.get(ti, 0) - 1
        
        for val in counter.values(): 
            if val != 0:
                return False
        return True
        
        
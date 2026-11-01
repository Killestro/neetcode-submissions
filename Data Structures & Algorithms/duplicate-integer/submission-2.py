class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapp = {}

        for num in nums:
            mapp[num] = mapp.get(num, 0) + 1
            if mapp[num] > 1:
                return True
        
        for value in mapp.values():
            if value > 1: 
                return True
        return False
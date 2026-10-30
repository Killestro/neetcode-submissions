class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1): # will iterate till last 2nd char
            for j in range(i + 1 , len(nums)): # will iterate from i + 1 to last char
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        

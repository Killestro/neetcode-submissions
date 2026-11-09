class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            req_num = target - num
            if req_num in num_map:
                return [num_map[req_num], i]
            num_map[num] = i
                
        

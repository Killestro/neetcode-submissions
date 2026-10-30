class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, current_number in enumerate(nums):
            required_number = target - current_number

            if required_number in num_map:
                return [num_map[required_number], i]
            
            num_map[current_number] = i
                
        
